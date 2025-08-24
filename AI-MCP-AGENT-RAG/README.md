# AI Agent, RAG, MCP 학습 프로젝트

## 프로젝트 목표
AI Agent, RAG(Retrieval-Augmented Generation), MCP(Model Context Protocol) 개념을 학습하고 실제 구현해보는 프로젝트입니다.

## 🚀 현재 구현 상태

### ✅ 완료된 기능
- **RAG 시스템 핵심 구현**
  - 문서 처리 및 청킹 (PDF, DOCX, TXT, MD 지원)
  - **로컬 임베딩 모델** (Sentence Transformers) - API 키 불필요!
  - ChromaDB 벡터 데이터베이스
  - LangChain 기반 질의응답 체인
  - 웹 인터페이스 (FastAPI + HTML/JS)
  - 콘솔 예제 스크립트

- **MCP 프로토콜 구현**
  - 기본 MCP 서버/클라이언트 구조
  - 파일 시스템 도구들 (읽기, 쓰기, 디렉토리 관리)
  - 웹 API 도구들 (날씨, 뉴스, Slack 시뮬레이션)
  - JSON 기반 요청/응답 처리
  - 에러 처리 및 파라미터 검증

- **AI Agent 프레임워크**
  - ReAct 패턴 (Reasoning + Acting) 구현
  - RAG 시스템과 MCP 서버 통합
  - 자율적 작업 수행 및 목표 달성
  - 실행 과정 추적 및 결과 분석
  - 대화형 Agent 인터페이스

### ✅ 학습 완료!
- [x] RAG 시스템 구현
- [x] MCP 프로토콜 학습 및 구현
- [x] AI Agent 개발

## 📁 프로젝트 구조

```
AI-MCP-AGENT-RAG/
├── src/                    # 핵심 소스 코드
│   ├── rag_system.py      # RAG 시스템 메인 클래스
│   ├── web_interface.py   # 웹 인터페이스
│   ├── mcp/               # MCP 프로토콜 구현
│   │   ├── mcp_server.py  # MCP 서버 기본 구현
│   │   └── tools/         # MCP 도구들
│   └── ai_agent/          # AI Agent 프레임워크
│       └── agent_framework.py  # Agent 기본 구현
├── examples/               # 예제 및 테스트
│   ├── rag_example.py     # RAG 시스템 테스트 예제
│   ├── mcp/               # MCP 예제들
│   │   ├── basic_mcp_example.py      # 기본 MCP 예제
│   │   └── web_api_mcp_example.py    # 웹 API MCP 예제
│   └── ai_agent/          # AI Agent 예제들
│       └── integrated_agent_example.py  # 통합 Agent 예제
├── docs/                   # 문서 및 개념 설명
│   ├── RAG_개념.md        # RAG 개념 설명
│   └── AI_Agent_개념.md   # AI Agent 개념 설명
├── requirements.txt        # Python 패키지 의존성
├── env_example.txt        # 환경 변수 설정 예시
├── run_rag.py             # 메인 실행 스크립트
└── README.md              # 프로젝트 설명서
```

## 🛠️ 기술 스택

- **Python 3.8+**
- **LangChain**: AI 체인 및 도구
- **Sentence Transformers**: 로컬 임베딩 모델 (API 키 불필요!)
- **ChromaDB**: 벡터 데이터베이스
- **FastAPI**: 웹 API 프레임워크
- **HTML/CSS/JS**: 프론트엔드 인터페이스
- **Ollama** (선택사항): 로컬 LLM 실행

## 🚀 시작하기

### 1. 환경 설정

```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화 (macOS/Linux)
source venv/bin/activate

# 가상환경 활성화 (Windows)
venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt
```

### 2. 실행 (API 키 불필요!)

```bash
# 메인 실행 스크립트
python run_rag.py

# 또는 직접 실행
python examples/rag_example.py          # 콘솔 모드
python -m uvicorn src.web_interface:app --reload  # 웹 인터페이스
```

## 💡 시스템 특징

### 🔓 **완전 무료 & 오프라인**
- **API 키 불필요**: OpenAI나 다른 클라우드 서비스 계정 불필요
- **로컬 실행**: 모든 처리가 로컬 컴퓨터에서 실행
- **오프라인 작동**: 인터넷 연결 없이도 작동

### 🤖 **두 가지 모드 지원**
1. **LLM 모드** (Ollama 설치 시)
   - 고품질 AI 답변 생성
   - 자연스러운 대화형 응답

2. **키워드 매칭 모드** (기본)
   - 빠른 키워드 기반 검색
   - 관련 문서에서 직접 답변 추출

## 📖 사용 방법

### 콘솔 모드
1. `python run_rag.py` 실행
2. "1" 선택 (콘솔 모드)
3. 자동으로 샘플 문서 생성 및 테스트 실행

### 웹 인터페이스
1. `python run_rag.py` 실행
2. "2" 선택 (웹 인터페이스)
3. 브라우저에서 `http://localhost:8000` 접속
4. 문서 업로드 후 질의응답

## 🔍 RAG 시스템 작동 원리

1. **문서 처리**: 다양한 형식의 문서를 텍스트로 변환
2. **청킹**: 긴 문서를 의미 있는 작은 단위로 분할
3. **임베딩**: **Sentence Transformers**로 텍스트를 벡터로 변환
4. **검색**: 질문과 유사한 문서 청크 검색
5. **생성**: 검색된 정보를 바탕으로 답변 생성

## 🚀 Ollama 설치 (선택사항)

고품질 LLM 답변을 원한다면 Ollama를 설치하세요:

```bash
# macOS
brew install ollama

# Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Windows
# https://ollama.ai/download 에서 다운로드

# 모델 다운로드
ollama pull llama2
```

## 📚 학습 자료

- **RAG 개념**: `docs/RAG_개념.md`
- **코드 예제**: `examples/rag_example.py`
- **웹 인터페이스**: `src/web_interface.py`

## 🔧 커스터마이징

### 임베딩 모델 변경
```python
# src/rag_system.py에서
self.embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2",  # 더 큰 모델
    model_kwargs={'device': 'cuda'}  # GPU 사용
)
```

### 청크 크기 조정
```python
# src/rag_system.py에서
self.document_processor = DocumentProcessor(
    chunk_size=1000,      # 청크 크기
    chunk_overlap=200     # 청크 간 겹침
)
```

## 🐛 문제 해결

### 일반적인 오류
1. **패키지 오류**: `pip install -r requirements.txt` 재실행
2. **포트 충돌**: 다른 포트 사용 또는 기존 프로세스 종료
3. **메모리 부족**: 더 작은 임베딩 모델 사용

### 성능 최적화
```bash
# GPU 사용 (CUDA 지원 시)
export CUDA_VISIBLE_DEVICES=0

# 더 작은 모델 사용
# all-MiniLM-L6-v2 (기본) → all-MiniLM-L6-v2 (권장)
```

## 🎉 학습 완료!

축하합니다! AI Agent, RAG, MCP 학습을 모두 완료했습니다!

### 🚀 실행 방법

```bash
# RAG 시스템 실행
python run_rag.py

# MCP 기본 예제
python examples/mcp/basic_mcp_example.py

# 통합 AI Agent 실행
python examples/ai_agent/integrated_agent_example.py
```

### 🔮 확장 가능한 기능들
- 실제 LLM 연동 (OpenAI, Anthropic 등)
- 멀티모달 지원 (이미지, 오디오)
- 실시간 학습 및 업데이트
- 멀티 Agent 협력 시스템
- 분산 처리 및 확장성

## 🤝 기여하기

이 프로젝트는 학습 목적으로 만들어졌습니다. 
개선 사항이나 버그 리포트는 언제든 환영합니다!

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.
