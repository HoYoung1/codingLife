"""
LangGraph StateGraph — A2A Multi-Agent 오케스트레이션
Analyzer → Expert → Strategist 순차 실행
"""

from langgraph.graph import StateGraph, END

from backend.models.state import ProcessState
from backend.agents.analyzer import run_analyzer
from backend.agents.expert import run_expert
from backend.agents.strategist import run_strategist


def build_graph():
    builder = StateGraph(ProcessState)

    builder.add_node("analyzer", run_analyzer)
    builder.add_node("expert", run_expert)
    builder.add_node("strategist", run_strategist)

    builder.set_entry_point("analyzer")
    builder.add_edge("analyzer", "expert")
    builder.add_edge("expert", "strategist")
    builder.add_edge("strategist", END)

    return builder.compile()


# 모듈 로드 시 1회 컴파일 (FastAPI lifespan 내에서 사용)
sentinel_graph = build_graph()
