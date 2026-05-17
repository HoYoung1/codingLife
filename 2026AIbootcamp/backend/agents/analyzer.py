"""
Node 1: Log Analyzer Agent
텍스트 로그에서 이벤트를 파싱하고 시계열 추세·이상치를 추출한다.
Tool Calling + ReAct 패턴으로 구현.
"""

import json
import re

from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langgraph.prebuilt import create_react_agent

from backend.config import get_llm
from backend.models.state import ProcessState

SYSTEM_PROMPT = """당신은 반도체 공정 데이터 분석 전문가입니다.
텍스트 형태의 장비 로그에서 시계열 이벤트를 파싱하고,
PM(예방 정비) 전후의 수치 변화 추세와 통계적 이상치를 식별하여
다음 단계 에이전트가 활용할 수 있는 정형화된 분석 결과를 생성하십시오.

[분석 절차 - Chain of Thought]
1. parse_log_entries 도구로 로그를 구조화된 이벤트 목록으로 변환하십시오.
2. detect_trend 도구로 수치의 방향성(우상향/안정/우하향)을 분석하십시오.
3. 분석 결과를 바탕으로 다음 JSON 형식으로 최종 답변을 작성하십시오:
{
  "parsed_events": [...],
  "trend_summary": "...",
  "anomalies": [...]
}

반드시 위 JSON 형식의 최종 답변을 출력해야 합니다."""


@tool
def parse_log_entries(raw_log: str) -> str:
    """텍스트 로그를 파싱하여 타임스탬프, 이벤트 유형, 센서명, 값, 상태를 JSON 리스트로 반환합니다."""
    events = []
    lines = raw_log.strip().split("\n")
    sensor_pattern = re.compile(
        r"\[(?P<ts>[^\]]+)\]\s+(?P<type>\w+):\s*(?P<value>[\d.]+)?\s*(?:\(Status:\s*(?P<status>[^)]+)\))?"
    )
    event_pattern = re.compile(r"\[(?P<ts>[^\]]+)\]\s+EVENT:\s*(?P<desc>.+)")

    for line in lines:
        line = line.strip()
        if not line:
            continue
        m = event_pattern.match(line)
        if m:
            events.append({"timestamp": m.group("ts").strip(), "type": "EVENT",
                           "description": m.group("desc").strip(), "value": None, "status": None})
            continue
        m = sensor_pattern.match(line)
        if m:
            val = m.group("value")
            events.append({"timestamp": m.group("ts").strip(), "type": m.group("type").strip(),
                           "description": None, "value": float(val) if val else None,
                           "status": m.group("status").strip() if m.group("status") else "Unknown"})
    return json.dumps(events, ensure_ascii=False)


@tool
def detect_trend(events_json: str, sensor_name: str = "SENSOR_PARTICLE") -> str:
    """지정 센서의 수치로 추세를 분석하고 이상치 목록을 반환합니다."""
    events = json.loads(events_json)
    sensor_events = [e for e in events if e.get("type") == sensor_name and e.get("value") is not None]

    if not sensor_events:
        return json.dumps({"trend": "데이터 없음", "anomalies": []}, ensure_ascii=False)

    values = [e["value"] for e in sensor_events]
    timestamps = [e["timestamp"] for e in sensor_events]
    pm_idx = next(
        (i for i, e in enumerate(events) if e.get("type") == "EVENT" and "PM" in str(e.get("description", ""))),
        None,
    )

    if len(values) >= 2:
        delta = values[-1] - values[0]
        pct = (delta / values[0]) * 100 if values[0] != 0 else 0
        if delta > 0.003:
            trend = f"우상향 ({values[0]:.3f} → {values[-1]:.3f}, +{pct:.1f}%)"
        elif delta < -0.003:
            trend = f"우하향 ({values[0]:.3f} → {values[-1]:.3f}, {pct:.1f}%)"
        else:
            trend = f"안정 ({values[0]:.3f} ~ {values[-1]:.3f})"
    else:
        trend = f"단일 측정값: {values[0]:.3f}"

    anomalies = []
    for e in sensor_events:
        v = e["value"]
        if v > 0.020:
            anomalies.append({"sensor": sensor_name, "timestamp": e["timestamp"],
                              "value": v, "threshold": 0.020, "severity": "CRITICAL"})
        elif v > 0.015:
            anomalies.append({"sensor": sensor_name, "timestamp": e["timestamp"],
                              "value": v, "threshold": 0.015, "severity": "HIGH"})

    return json.dumps({"trend": trend, "pm_detected": pm_idx is not None,
                       "value_series": list(zip(timestamps, values)), "anomalies": anomalies},
                      ensure_ascii=False)


def run_analyzer(state: ProcessState) -> dict:
    llm = get_llm(large=False)
    agent = create_react_agent(llm, [parse_log_entries, detect_trend])
    result = agent.invoke({
        "messages": [HumanMessage(content=f"다음 장비 로그를 분석하십시오:\n\n{state['raw_log']}")]
    })

    last_content = result["messages"][-1].content
    try:
        json_match = re.search(r"\{[\s\S]*\}", last_content)
        if json_match:
            parsed = json.loads(json_match.group())
            return {
                "parsed_events": parsed.get("parsed_events", []),
                "trend_summary": parsed.get("trend_summary", last_content),
                "anomalies": parsed.get("anomalies", []),
            }
    except (json.JSONDecodeError, AttributeError):
        pass

    return {"parsed_events": [], "trend_summary": last_content, "anomalies": []}
