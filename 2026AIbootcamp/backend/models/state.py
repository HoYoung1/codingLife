from typing import Literal, Optional
from typing_extensions import TypedDict
from pydantic import BaseModel, Field


class AnomalyDetail(BaseModel):
    sensor: str = Field(description="센서 이름 (예: SENSOR_PARTICLE)")
    current_value: float = Field(description="현재 측정값")
    threshold: float = Field(description="기준 한계치")
    severity: Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"] = Field(
        description="이상 심각도"
    )


class FinalReport(BaseModel):
    summary: str = Field(description="전조 증상 및 현재 상황 요약 (2~3문장)")
    root_cause_hypothesis: str = Field(description="근본 원인 가설 (매뉴얼 근거 포함)")
    anomalies: list[AnomalyDetail] = Field(description="감지된 이상치 목록")
    recommended_actions: list[str] = Field(description="운영자 즉시 수행 권고 조치 (우선순위 순)")
    urgency: Literal["MONITOR", "INSPECT", "HALT"] = Field(
        description="긴급도: MONITOR(관찰), INSPECT(점검), HALT(즉시 중단)"
    )
    confidence_score: float = Field(description="분석 신뢰도 0.0~1.0", ge=0.0, le=1.0)
    referenced_standards: list[str] = Field(description="참조한 표준 문서명")


# LangGraph 3-노드 파이프라인 공유 상태
class ProcessState(TypedDict):
    # 입력
    raw_log: str

    # Node 1 (Analyzer) 출력
    parsed_events: list[dict]
    trend_summary: str
    anomalies: list[dict]

    # Node 2 (Expert) 출력
    rag_context: str
    expert_opinion: str
    relevant_standards: list[str]

    # Node 3 (Strategist) 출력
    final_report: Optional[FinalReport]
