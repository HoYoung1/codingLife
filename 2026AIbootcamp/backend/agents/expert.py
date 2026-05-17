"""
Node 2: Standard Expert Agent
RAG로 매뉴얼을 검색하여 Analyzer 결과와 대조, 도메인 전문 의견을 생성한다.
"""

import json
import re

from langchain_core.prompts import ChatPromptTemplate

from backend.config import get_llm
from backend.models.state import ProcessState
from backend.rag.retriever import retrieve_context

SYSTEM_PROMPT = """당신은 반도체 공정 표준 및 장비 매뉴얼 전문가입니다.
Log Analyzer가 감지한 이상 징후와 관련 매뉴얼 내용을 대조하여
현재 상태가 어떤 공정 표준 위반에 해당하는지 판단하고,
근거 문서를 명시하여 다음 단계 에이전트에게 전문적인 의견을 제공하십시오.

[분석 기준]
- PM 이후 파티클 우상향이 감지된 경우: 세정 불량 패턴(패턴 A)과의 일치 여부 확인
- 한계치(0.020) 초과 여부와 추세 방향을 반드시 언급
- 참조한 매뉴얼 문서명과 해당 항목을 명시할 것

[출력 형식]
반드시 다음 JSON 형식으로만 출력하십시오. 다른 텍스트 없이 JSON만 출력:
{{
  "expert_opinion": "전문가 의견 (3~5문장)",
  "relevant_standards": ["참조 문서명 §항목번호", ...]
}}"""

HUMAN_TEMPLATE = """[Analyzer 분석 결과]
추세 요약: {trend_summary}
감지된 이상치: {anomalies}

[참조 가능한 매뉴얼 내용]
{rag_context}

위 내용을 바탕으로 전문가 의견을 JSON 형식으로 작성하십시오."""


def run_expert(state: ProcessState) -> dict:
    query = f"{state['trend_summary']} {json.dumps(state['anomalies'], ensure_ascii=False)}"
    rag_context = retrieve_context(query, k=4)

    llm = get_llm(large=False, json_mode=True)
    prompt = ChatPromptTemplate.from_messages([("system", SYSTEM_PROMPT), ("human", HUMAN_TEMPLATE)])
    chain = prompt | llm

    response = chain.invoke({
        "trend_summary": state["trend_summary"],
        "anomalies": json.dumps(state["anomalies"], ensure_ascii=False),
        "rag_context": rag_context,
    })

    content = response.content
    try:
        json_match = re.search(r"\{[\s\S]*\}", content)
        if json_match:
            parsed = json.loads(json_match.group())
            return {
                "rag_context": rag_context,
                "expert_opinion": parsed.get("expert_opinion", content),
                "relevant_standards": parsed.get("relevant_standards", []),
            }
    except (json.JSONDecodeError, AttributeError):
        pass

    return {"rag_context": rag_context, "expert_opinion": content, "relevant_standards": []}
