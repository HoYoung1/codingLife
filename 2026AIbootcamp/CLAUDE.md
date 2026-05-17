# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Semi-Quality Sentinel** — 반도체 공정 품질 전조 증상 분석기 (AI Bootcamp 최종 과제)

텍스트 기반 장비 로그를 입력받아 3개의 LangGraph Agent가 A2A 협업으로 품질 이상 전조 증상을 감지하고 대응 권고 리포트를 자동 생성하는 Multi-Agent AI 서비스.

## Architecture

```
Streamlit UI → FastAPI Backend → LangGraph Router
                                      ↓
                          ┌─────────────────────────────┐
                          │     A2A Agentic Workflow     │
                          │                             │
                          │  [1] Log Analyzer Agent     │ ← 시계열 트렌드·이상치 추출
                          │         ↓                   │
                          │  [2] Standard Expert Agent  │ ← RAG (FAISS/Chroma) + 매뉴얼 대조
                          │         ↓                   │
                          │  [3] Strategy Response Agent│ → JSON 구조화 리포트 생성
                          └─────────────────────────────┘
                                      ↓
                              Streamlit UI (결과 시각화)
```

### Agent 역할

| Agent | 역할 | 핵심 기능 |
|---|---|---|
| Log Analyzer | 로그 파싱 및 트렌드 분석 | PM 이후 수치 우상향, 이상치 포착 |
| Standard Expert | RAG 기반 도메인 지식 매칭 | 매뉴얼·규격서 검색 후 현상 판단 |
| Strategy Response | 최종 의사결정 및 리포트 | JSON 구조화 출력, 운영자 보고서 |

### State 공유 구조

LangGraph `TypedDict` 기반 `ProcessState` 객체를 세 노드가 순차적으로 읽고 업데이트하며 분석 결과의 일관성을 유지한다.

## Tech Stack

- **LLM**: Azure OpenAI (GPT-4o, GPT-4o-mini)
- **Agent 오케스트레이션**: LangGraph (Multi-Agent), LangChain
- **Vector DB**: FAISS 또는 Chroma (로컬)
- **Embedding**: `text-embedding-3-small`
- **Backend**: FastAPI (Python 3.10+)
- **Frontend**: Streamlit
- **환경 변수**: python-dotenv

## Environment Variables

`.env` 파일에 아래 변수를 설정 (값은 homework.txt 참조, 절대 커밋하지 말 것):

```
AOAI_ENDPOINT=
AOAI_API_KEY=
AOAI_DEPLOY_GPT4O_MINI=gpt-4o-mini
AOAI_DEPLOY_GPT4O=gpt-4o
AOAI_DEPLOY_EMBED_3_LARGE=text-embedding-3-large
AOAI_DEPLOY_EMBED_3_SMALL=text-embedding-3-small
AOAI_DEPLOY_EMBED_ADA=text-embedding-ada-002
```

## Expected Project Structure

```
2026AIbootcamp/
├── .env                    # API 키 (gitignore)
├── docs/                   # 기획·설계 문서
├── data/                   # 가상 장비 매뉴얼 (PDF/TXT)
├── backend/
│   ├── main.py             # FastAPI 엔트리포인트
│   ├── agents/
│   │   ├── graph.py        # LangGraph 워크플로우 정의
│   │   ├── analyzer.py     # Log Analyzer Agent
│   │   ├── expert.py       # Standard Expert Agent
│   │   └── strategist.py   # Strategy Response Agent
│   ├── rag/
│   │   ├── ingest.py       # 문서 로드·청킹·임베딩·저장
│   │   └── retriever.py    # 유사도 검색 로직
│   └── models/
│       └── state.py        # ProcessState TypedDict
├── frontend/
│   └── app.py              # Streamlit UI
└── Dockerfile              # (선택)
```

## Common Commands

### 의존성 설치
```bash
pip install -r requirements.txt
```

### RAG 데이터 인덱싱 (최초 1회 또는 데이터 변경 시)
```bash
python backend/rag/ingest.py
```

### FastAPI 백엔드 실행
```bash
uvicorn backend.main:app --reload --port 8000
```

### Streamlit 프론트엔드 실행
```bash
streamlit run frontend/app.py
```

### Docker Compose (전체 서비스 한 번에 실행)
```bash
# 최초 실행 — 이미지 빌드 + Ollama 모델 다운로드 (~5GB) + 서비스 시작
docker compose up --build

# 이후 실행
docker compose up -d

# 종료
docker compose down
```

서비스 기동 순서: `ollama` → `model-loader` (모델 pull) → `backend` → `frontend`
- Streamlit UI: http://localhost:8501
- FastAPI Swagger: http://localhost:8000/docs
- Ollama: http://localhost:11434

Docker 환경에서 `OLLAMA_BASE_URL`은 자동으로 `http://ollama:11434`로 설정되어 `.env` 값을 덮어씀.

## Key Implementation Notes

- **Prompt 전략**: 각 Agent에 역할 기반 시스템 프롬프트 부여 + CoT 유도 (수치 변화 → 과거 이벤트 대조 → 인과 추론).
- **Structured Output**: Strategy Response Agent는 반드시 JSON 스키마(Pydantic 모델)로 출력하여 Streamlit 시각화와 연동.
- **RAG 검색 흐름**: 로그 텍스트에서 추출한 키워드/현상을 쿼리로 변환 → FAISS similarity search → 상위 k개 청크를 Expert Agent context로 주입.
- **임베딩 동시 사용량 제한**: `text-embedding-3-small` 호출이 응답 없을 경우 다른 시간대에 재시도.
- **A2A 협업 평가 요소**: 단일 Agent로 구현하면 과제 미인정 — 반드시 3개 노드가 State를 공유하며 순차 실행되어야 함.
