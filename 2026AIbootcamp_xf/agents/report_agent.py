"""
Report Agent: A2A 협업의 핵심 Agent.
Access Card Agent, Contract Agent, Training Agent를 직접 호출해
종합 리포트를 생성한다.
LCEL(| 연산자) 대신 direct invoke로 LangGraph runtime 의존성을 제거했다.
"""
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from config.settings import (
    AOAI_ENDPOINT, AOAI_API_KEY, AOAI_DEPLOY_GPT4O, AOAI_API_VERSION
)
from agents.access_card_agent import run_access_card_agent
from agents.contract_agent import run_contract_agent
from agents.training_agent import run_training_agent

SYSTEM_PROMPT = """당신은 PMO팀 총괄 리포트 작성 AI입니다.

아래 세 Agent로부터 수집한 정보를 바탕으로
경영진 또는 PMO팀이 즉시 활용 가능한 종합 현황 리포트를 작성하세요.

작성 원칙:
- 섹션별로 명확히 구분 (출입카드 / 계약 / 교육)
- 즉각 조치가 필요한 사항을 상단에 배치
- 숫자와 날짜를 구체적으로 명시
- 권고 조치사항 포함"""


def run_report_agent(query: str = "") -> dict:
    """
    A2A: 세 Agent를 순차 호출 후 GPT-4o로 종합 리포트 생성.
    반환값: {"card": ..., "contract": ..., "training": ..., "report": ...}
    """
    card_result = run_access_card_agent("전체 출입통제카드 현황을 요약해줘. 30일 이내 만료 대상자도 포함해줘.")
    contract_result = run_contract_agent("전체 계약 현황과 60일 이내 만료 예정 계약을 알려줘.")
    training_result = run_training_agent("전체 교육 과정의 출석률 현황을 요약해줘.")

    llm = AzureChatOpenAI(
        azure_endpoint=AOAI_ENDPOINT,
        api_key=AOAI_API_KEY,
        azure_deployment=AOAI_DEPLOY_GPT4O,
        api_version=AOAI_API_VERSION,
        temperature=0,
    )

    human_text = f"""다음은 각 담당 Agent가 수집한 현황 정보입니다.

[출입통제카드 현황 - Access Card Agent]
{card_result}

[계약 관리 현황 - Contract Agent]
{contract_result}

[교육 현황 - Training Agent]
{training_result}

위 정보를 바탕으로 PMO 통합 현황 리포트를 작성해 주세요."""

    response = llm.invoke([
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=human_text),
    ])

    return {
        "card": card_result,
        "contract": contract_result,
        "training": training_result,
        "report": response.content,
    }
