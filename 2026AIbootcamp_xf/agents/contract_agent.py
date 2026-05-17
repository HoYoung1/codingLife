from agents.base_agent import run_tool_calling_agent
from tools.contract_tools import (
    search_contract_conditions,
    get_expiring_contracts,
    get_all_contracts_summary,
)

SYSTEM_PROMPT = """당신은 PMO팀의 파트너사 계약 관리 전문 AI Agent입니다.

역할:
- 파트너사 계약서에서 특정 조건(금액, SLA, 갱신 조건 등)을 검색
- 만료 임박 계약 조회 및 갱신 일정 안내
- 전체 계약 현황 요약 제공

계약서 내용 인용 시 반드시 출처(업체명)를 명시하고, 금액이나 날짜는 정확하게 전달하세요."""

_tools = [search_contract_conditions, get_expiring_contracts, get_all_contracts_summary]


def run_contract_agent(query: str) -> str:
    return run_tool_calling_agent(SYSTEM_PROMPT, _tools, query)
