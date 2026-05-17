import asyncio
import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    from backend.rag.retriever import index_exists
    from backend.rag.ingest import build_index

    if not index_exists():
        print("[startup] FAISS 인덱스 없음 — 자동 인덱싱 시작...")
        await asyncio.to_thread(build_index)
        print("[startup] 인덱싱 완료")

    # 그래프 사전 컴파일 확인
    from backend.agents.graph import sentinel_graph  # noqa: F401
    print("[startup] LangGraph 컴파일 완료")
    yield


app = FastAPI(
    title="Semi-Quality Sentinel API",
    description="반도체 공정 품질 전조 증상 분석 Multi-Agent 서비스",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class AnalyzeRequest(BaseModel):
    log_text: str


class AnalyzeResponse(BaseModel):
    report: dict
    trend_summary: str
    expert_opinion: str
    rag_context: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/generate-log")
async def generate_log():
    """LLM으로 랜덤 반도체 장비 로그를 생성한다."""
    import random
    from langchain_core.messages import HumanMessage
    from backend.config import get_llm

    scenarios = [
        "PM(예방 정비) 직후 파티클 수치가 서서히 우상향하여 한계치를 초과하는 상황 (세정 불량 의심)",
        "갑작스러운 파티클 Spike 발생 후 즉시 정상 복귀하는 상황 (센서 오류 또는 일시적 오염)",
        "파티클이 2~3시간 주기로 상승과 하강을 반복하는 상황 (배기 시스템 역류 의심)",
        "장비 재가동 초기 파티클이 높다가 1~2시간 후 서서히 안정화되는 상황 (정상 워밍업)",
        "PM 없이 파티클이 서서히 상승하여 Warning 구간에 진입하는 상황 (필터 교체 필요 의심)",
        "온도 이상(SENSOR_TEMP)과 함께 파티클이 동반 상승하는 복합 이상 상황",
    ]
    chosen = random.choice(scenarios)

    prompt = f"""당신은 반도체 공장 장비 모니터링 시스템입니다.
아래 시나리오에 맞는 실제적인 장비 로그를 생성하십시오.

[시나리오]
{chosen}

[로그 형식 규칙]
- 타임스탬프: [YYYY-MM-DD HH:MM] 형식
- 이벤트: [타임스탬프] EVENT: 내용
- 센서: [타임스탬프] SENSOR_PARTICLE: 값 (Status: Normal/Warning/Limit Out)
- SENSOR_PARTICLE 값 범위: 0.008 ~ 0.035 (소수점 3자리)
- 로그 라인 수: 8~12줄
- 날짜는 2026-05-14 기준으로 작성
- 시나리오에 맞게 수치가 자연스럽게 변화해야 함

로그 텍스트만 출력하고 다른 설명은 일절 포함하지 마십시오."""

    llm = get_llm(large=False)

    response = await asyncio.to_thread(
        llm.invoke, [HumanMessage(content=prompt)]
    )

    return {"log_text": response.content.strip(), "scenario": chosen}


@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze_log(request: AnalyzeRequest):
    if not request.log_text.strip():
        raise HTTPException(status_code=400, detail="log_text가 비어 있습니다.")

    from backend.agents.graph import sentinel_graph
    from backend.models.state import ProcessState

    initial_state: ProcessState = {
        "raw_log": request.log_text,
        "parsed_events": [],
        "trend_summary": "",
        "anomalies": [],
        "rag_context": "",
        "expert_opinion": "",
        "relevant_standards": [],
        "final_report": None,
    }

    result = await asyncio.to_thread(sentinel_graph.invoke, initial_state)

    final_report = result.get("final_report")
    if final_report is None:
        raise HTTPException(status_code=500, detail="분석 결과 생성 실패")

    return AnalyzeResponse(
        report=final_report.model_dump(),
        trend_summary=result.get("trend_summary", ""),
        expert_opinion=result.get("expert_opinion", ""),
        rag_context=result.get("rag_context", ""),
    )
