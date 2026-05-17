from agents.base_agent import run_tool_calling_agent
from tools.training_tools import (
    get_enrollment_status,
    get_attendance_ranking,
    get_training_summary,
)

SYSTEM_PROMPT = """당신은 PMO팀의 어학 교육 관리 전문 AI Agent입니다.

역할:
- 수강 신청 현황 조회 및 관리
- 과정별 출석률 추적 및 순위 제공
- 교육 현황 요약 리포트 생성

출석률이 낮은 수강생(70% 미만)은 별도로 강조하고, 순위는 구체적으로 명시하세요."""

_tools = [get_enrollment_status, get_attendance_ranking, get_training_summary]


def run_training_agent(query: str) -> str:
    return run_tool_calling_agent(SYSTEM_PROMPT, _tools, query)
