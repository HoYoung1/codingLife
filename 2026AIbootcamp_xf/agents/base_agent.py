"""
LangGraph/AgentExecutor 없이 동작하는 Tool Calling 기반 Agent 실행기.
OpenAI의 native function calling을 사용해 서버 호환성 문제를 우회한다.
"""
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from config.settings import (
    AOAI_ENDPOINT, AOAI_API_KEY, AOAI_DEPLOY_GPT4O_MINI, AOAI_API_VERSION
)

MAX_ITERATIONS = 10


def get_llm():
    return AzureChatOpenAI(
        azure_endpoint=AOAI_ENDPOINT,
        api_key=AOAI_API_KEY,
        azure_deployment=AOAI_DEPLOY_GPT4O_MINI,
        api_version=AOAI_API_VERSION,
        temperature=0,
    )


def run_tool_calling_agent(system_prompt: str, tools: list, query: str) -> str:
    """
    Tool Calling 루프:
    1. LLM이 tool_calls를 반환하면 해당 tool 실행
    2. 결과를 ToolMessage로 추가
    3. LLM이 tool 없이 응답하면 최종 답변 반환
    """
    tools_by_name = {t.name: t for t in tools}
    llm = get_llm().bind_tools(tools)

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=query),
    ]

    for _ in range(MAX_ITERATIONS):
        response = llm.invoke(messages)
        messages.append(response)

        if not response.tool_calls:
            return response.content

        for tc in response.tool_calls:
            tool = tools_by_name.get(tc["name"])
            if tool is None:
                result = f"도구 '{tc['name']}'를 찾을 수 없습니다."
            else:
                result = tool.invoke(tc["args"])
            messages.append(
                ToolMessage(content=str(result), tool_call_id=tc["id"])
            )

    return messages[-1].content if messages else "응답을 생성할 수 없습니다."
