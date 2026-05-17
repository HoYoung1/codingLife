"""
PMO Orchestrator: LLM 기반 의도 분류 후 적절한 Agent로 라우팅.
LangGraph StateGraph 대신 순수 Python으로 구현해 서버 호환성을 확보했다.
A2A 구조는 Report Agent가 나머지 세 Agent를 직접 호출하는 방식으로 유지된다.
"""
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from config.settings import (
    AOAI_ENDPOINT, AOAI_API_KEY, AOAI_DEPLOY_GPT4O_MINI, AOAI_API_VERSION
)

INTENT_PROMPT = """당신은 PMO 업무 분류기입니다.
사용자 질문을 읽고 가장 적합한 카테고리 하나만 반환하세요.

카테고리:
- card      : 출입통제카드 관련 (갱신, 만료, 직원 카드 조회, 알림)
- contract  : 계약 관련 (파트너사, 계약 조건, 만료, 금액, SLA)
- training  : 교육 관련 (출석, 수강 신청, 어학, 순위)
- report    : 전체 통합 현황, 요약 리포트 요청

질문: {query}

카테고리(단어 하나만):"""

FALLBACK_MSG = (
    "죄송합니다. 해당 질문은 PMO AI Hub의 관리 범위를 벗어난 것 같습니다.\n"
    "출입통제카드, 파트너사 계약, 어학 교육, 전체 현황 리포트에 대해 질문해 주세요."
)


def _get_llm():
    return AzureChatOpenAI(
        azure_endpoint=AOAI_ENDPOINT,
        api_key=AOAI_API_KEY,
        azure_deployment=AOAI_DEPLOY_GPT4O_MINI,
        api_version=AOAI_API_VERSION,
        temperature=0,
    )


def _classify_intent(query: str) -> str:
    llm = _get_llm()
    response = llm.invoke(INTENT_PROMPT.format(query=query))
    intent = response.content.strip().lower()
    return intent if intent in {"card", "contract", "training", "report"} else "unknown"


def run_pmo_agent(query: str, history: list = None) -> str:
    """
    사용자 쿼리를 분류해 적절한 Agent로 라우팅한다.

    Agent 간 협업(A2A) 흐름:
    - card     → Access Card Agent
    - contract → Contract Agent (RAG 기반)
    - training → Training Agent
    - report   → Report Agent (Access Card + Contract + Training 순차 호출)
    """
    from agents.access_card_agent import run_access_card_agent
    from agents.contract_agent import run_contract_agent
    from agents.training_agent import run_training_agent
    from agents.report_agent import run_report_agent

    intent = _classify_intent(query)

    if intent == "card":
        return run_access_card_agent(query)
    elif intent == "contract":
        return run_contract_agent(query)
    elif intent == "training":
        return run_training_agent(query)
    elif intent == "report":
        result = run_report_agent(query)
        return result["report"]
    else:
        return FALLBACK_MSG
