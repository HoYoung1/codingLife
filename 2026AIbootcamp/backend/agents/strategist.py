"""
Node 3: Strategy Response Agent
Analyzer + Expert 결과를 종합하여 최종 리포트를 생성한다.
- Azure: with_structured_output(FinalReport) 사용
- Ollama: format="json" + 수동 파싱 (with_structured_output 불안정)
"""

import json
import re

from langchain_core.prompts import ChatPromptTemplate

from backend.config import get_llm, LLM_PROVIDER
from backend.models.state import FinalReport, AnomalyDetail, ProcessState

SYSTEM_PROMPT = """당신은 반도체 공장 품질 관리 책임자입니다.
Log Analyzer와 Standard Expert의 분석 결과를 종합하여
운영자가 즉시 실행할 수 있는 단계별 대응 방안과
품질 리스크 수준을 평가한 공식 보고서를 JSON 형식으로 작성하십시오.

[보고서 작성 원칙]
- urgency는 반드시 MONITOR / INSPECT / HALT 중 정확히 하나만 사용
  · HALT: 파티클 한계치 초과 또는 급속 상승 추세
  · INSPECT: 경고 구간 진입 또는 PM 이후 상승 추세
  · MONITOR: 정상 범위이나 추세 변화 감지
- recommended_actions는 우선순위 순으로 나열
- confidence_score는 0.0~1.0 사이 숫자
- anomalies의 severity는 LOW / MEDIUM / HIGH / CRITICAL 중 하나
- current_value, threshold, confidence_score: 반드시 소수점 숫자 (예: 0.021) — 문자열 금지

[출력 형식] 다른 텍스트 없이 JSON만 출력:
{{
  "summary": "전반적 상황 요약 2~3문장",
  "root_cause_hypothesis": "근본 원인 가설",
  "anomalies": [{{"sensor": "SENSOR_PARTICLE", "current_value": 0.021, "threshold": 0.020, "severity": "HIGH"}}],
  "recommended_actions": ["조치1", "조치2"],
  "urgency": "INSPECT",
  "confidence_score": 0.85,
  "referenced_standards": ["문서명 §항목"]
}}"""

HUMAN_TEMPLATE = """[Log Analyzer 결과]
추세 요약: {trend_summary}
이상치 목록: {anomalies}

[Standard Expert 의견]
{expert_opinion}
참조 표준: {relevant_standards}

위 내용을 종합하여 최종 품질 진단 보고서를 JSON으로 작성하십시오."""


def _safe_float(val, default: float = 0.0) -> float:
    if val is None:
        return default
    try:
        return float(val)
    except (TypeError, ValueError):
        m = re.search(r"[\d.]+", str(val))
        return float(m.group()) if m else default


def _safe_severity(val: str) -> str:
    upper = str(val).upper()
    return upper if upper in {"LOW", "MEDIUM", "HIGH", "CRITICAL"} else "MEDIUM"


def _safe_urgency(val: str) -> str:
    upper = str(val).upper()
    return upper if upper in {"MONITOR", "INSPECT", "HALT"} else "MONITOR"


def _build_report_from_dict(data: dict, state: ProcessState) -> FinalReport:
    raw_anomalies = data.get("anomalies") or state.get("anomalies") or []
    anomalies = [
        AnomalyDetail(
            sensor=str(a.get("sensor", "UNKNOWN")),
            current_value=_safe_float(a.get("current_value") or a.get("value"), 0.0),
            threshold=_safe_float(a.get("threshold"), 0.020),
            severity=_safe_severity(a.get("severity", "MEDIUM")),
        )
        for a in raw_anomalies
    ]
    return FinalReport(
        summary=data.get("summary", ""),
        root_cause_hypothesis=data.get("root_cause_hypothesis", ""),
        anomalies=anomalies,
        recommended_actions=data.get("recommended_actions") or [],
        urgency=_safe_urgency(data.get("urgency", "MONITOR")),
        confidence_score=min(1.0, max(0.0, _safe_float(data.get("confidence_score"), 0.7))),
        referenced_standards=data.get("referenced_standards") or [],
    )


def run_strategist(state: ProcessState) -> dict:
    prompt = ChatPromptTemplate.from_messages([("system", SYSTEM_PROMPT), ("human", HUMAN_TEMPLATE)])
    invoke_kwargs = {
        "trend_summary": state["trend_summary"],
        "anomalies": json.dumps(state["anomalies"], ensure_ascii=False),
        "expert_opinion": state["expert_opinion"],
        "relevant_standards": json.dumps(state["relevant_standards"], ensure_ascii=False),
    }

    # ── Azure: with_structured_output 사용 ──────────────────────
    if LLM_PROVIDER == "azure":
        llm = get_llm(large=True)
        chain = prompt | llm.with_structured_output(FinalReport)
        try:
            final_report: FinalReport = chain.invoke(invoke_kwargs)
            return {"final_report": final_report}
        except Exception:
            pass  # 실패 시 JSON 수동 파싱으로 fallback

    # ── Ollama (또는 Azure fallback): format="json" + 수동 파싱 ──
    llm = get_llm(large=True, json_mode=True)
    chain = prompt | llm
    response = chain.invoke(invoke_kwargs)
    content = response.content

    try:
        json_match = re.search(r"\{[\s\S]*\}", content)
        if json_match:
            data = json.loads(json_match.group())
            return {"final_report": _build_report_from_dict(data, state)}
    except Exception:
        pass

    # 완전 실패 시 Analyzer/Expert 데이터로 최소 리포트 구성
    fallback_anomalies = [
        AnomalyDetail(
            sensor=str(a.get("sensor", "UNKNOWN")),
            current_value=_safe_float(a.get("value") or a.get("current_value"), 0.0),
            threshold=_safe_float(a.get("threshold"), 0.020),
            severity=_safe_severity(a.get("severity", "MEDIUM")),
        )
        for a in (state.get("anomalies") or [])
    ]
    return {"final_report": FinalReport(
        summary=state.get("expert_opinion", "")[:300] or "분석 결과를 확인하세요.",
        root_cause_hypothesis=state.get("trend_summary", "")[:200] or "추세 분석 결과를 확인하세요.",
        anomalies=fallback_anomalies,
        recommended_actions=["전문가 점검 권고"],
        urgency="INSPECT" if fallback_anomalies else "MONITOR",
        confidence_score=0.4,
        referenced_standards=state.get("relevant_standards") or [],
    )}
