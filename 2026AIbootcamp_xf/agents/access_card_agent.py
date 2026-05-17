from agents.base_agent import run_tool_calling_agent
from tools.card_tools import (
    check_expiring_cards,
    get_employee_card,
    get_card_summary,
    generate_renewal_notification,
)

SYSTEM_PROMPT = """당신은 PMO팀의 출입통제카드 관리 전문 AI Agent입니다.

역할:
- 직원들의 출입통제카드 만료일 추적 및 갱신 알림
- 카드 현황 조회 및 요약 리포트 제공
- 갱신이 필요한 직원에게 보낼 알림 메시지 생성

답변 시 구체적인 직원명, 날짜, 잔여일수를 포함하여 실용적인 정보를 제공하세요."""

_tools = [check_expiring_cards, get_employee_card, get_card_summary, generate_renewal_notification]


def run_access_card_agent(query: str) -> str:
    return run_tool_calling_agent(SYSTEM_PROMPT, _tools, query)
