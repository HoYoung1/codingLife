TRD

1. TRD (Technical Requirements Document)
1.1 기술 스택 및 환경
* LLM: Azure OpenAI (GPT-4o, GPT-4o-mini)
* Framework: LangChain, LangGraph (Multi-Agent 오케스트레이션)
* Database: FAISS 또는 Chroma (Local Vector DB)
* Backend: FastAPI (Python 3.10+)
* Frontend: Streamlit
* Environment: 사내망 보안 가이드를 준수한 환경변수(python-dotenv) 관리
1.2 핵심 모듈 설계
1. Ingestion Module: 텍스트 로그 파일(.txt)을 읽어 실시간 또는 배치로 데이터를 파싱하는 기능.
2. RAG Module: 가상의 품질 매뉴얼 데이터를 text-embedding-3-small 모델을 사용하여 임베딩 후 Vector DB에 저장 및 검색.
3. Agentic Workflow (LangGraph):
    * Node 1 (Analyzer): 로그 내 시계열 데이터 추세 분석.
    * Node 2 (Expert): RAG를 통한 도메인 지식 매칭.
    * Node 3 (Strategist): 최종 의사결정 및 리포트 생성.
4. State Management: 에이전트 간 '공정 상태 객체(TypedDict)'를 공유하여 분석 결과의 일관성 유지.
