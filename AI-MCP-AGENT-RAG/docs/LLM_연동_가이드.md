# LLM 연동 가이드

## 개요
현재 구현된 Agent는 시뮬레이션 모드로 동작하지만, 실제 LLM을 연동하면 진짜 지능적인 Agent가 됩니다.

## 지원하는 LLM 제공자

### 1. OpenAI API
가장 강력하고 안정적인 선택

```python
from src.ai_agent.llm_agent import LLMAgent, LLMConfig, LLMProvider

# OpenAI 설정
config = LLMConfig(
    provider=LLMProvider.OPENAI,
    model="gpt-4",  # 또는 "gpt-3.5-turbo"
    api_key="your-openai-api-key",
    temperature=0.7,
    max_tokens=1500
)

agent = LLMAgent("OpenAI Agent", config, rag_system, mcp_server)
```

**필요한 패키지:**
```bash
pip install openai
```

**환경 변수 설정:**
```bash
export OPENAI_API_KEY="your-api-key-here"
```

### 2. Ollama (로컬 LLM)
완전 무료, 오프라인 실행 가능

```python
# Ollama 설정
config = LLMConfig(
    provider=LLMProvider.OLLAMA,
    model="llama2",  # 또는 "codellama", "mistral" 등
    temperature=0.7
)

agent = LLMAgent("Ollama Agent", config, rag_system, mcp_server)
```

**Ollama 설치:**
```bash
# macOS
brew install ollama

# Linux
curl -fsSL https://ollama.ai/install.sh | sh

# 모델 다운로드
ollama pull llama2
ollama pull codellama
```

### 3. 기타 LLM 제공자
코드를 확장하여 다른 제공자도 지원 가능:
- Anthropic Claude
- Google Gemini
- Hugging Face Transformers
- Azure OpenAI

## 실제 연동 예제

### OpenAI 연동 예제
```python
import os
from src.ai_agent.llm_agent import LLMAgent, LLMConfig, LLMProvider

# API 키 설정
os.environ["OPENAI_API_KEY"] = "your-api-key"

# 설정
config = LLMConfig(
    provider=LLMProvider.OPENAI,
    model="gpt-3.5-turbo",
    temperature=0.7
)

# Agent 생성
agent = LLMAgent("실제 OpenAI Agent", config, rag_system, mcp_server)

# 작업 실행
result = agent.execute_task("프로젝트 현황을 분석하고 개선사항을 제안해주세요")
print(result['final_summary'])
```

### Ollama 연동 예제
```python
# Ollama 설정 (API 키 불필요)
config = LLMConfig(
    provider=LLMProvider.OLLAMA,
    model="llama2",
    temperature=0.8
)

# Agent 생성
agent = LLMAgent("로컬 Llama Agent", config, rag_system, mcp_server)

# 작업 실행
result = agent.execute_task("코드 리뷰를 해주고 개선사항을 알려주세요")
```

## LLM별 특성 및 선택 가이드

### OpenAI GPT-4
- **장점**: 최고 수준의 추론 능력, 안정적인 성능
- **단점**: 비용 발생, 인터넷 연결 필요
- **적합한 용도**: 복잡한 분석, 창의적 작업, 프로덕션 환경

### OpenAI GPT-3.5-turbo
- **장점**: 빠른 속도, 합리적인 비용, 좋은 성능
- **단점**: GPT-4보다 제한적인 추론 능력
- **적합한 용도**: 일반적인 업무, 빠른 응답이 필요한 경우

### Ollama Llama2
- **장점**: 완전 무료, 오프라인 실행, 개인정보 보호
- **단점**: 상대적으로 낮은 성능, 로컬 리소스 필요
- **적합한 용도**: 개발/테스트, 개인정보 민감한 작업

### Ollama CodeLlama
- **장점**: 코드 특화, 무료, 오프라인
- **단점**: 코드 외 작업에서 제한적
- **적합한 용도**: 코드 리뷰, 프로그래밍 도움

## 성능 최적화 팁

### 1. 프롬프트 최적화
```python
# 좋은 프롬프트 예시
system_prompt = """당신은 전문적인 AI Agent입니다.
주어진 작업을 단계별로 분석하고 최적의 도구를 선택하여 실행하세요.
각 단계에서 명확한 추론 과정을 설명하세요."""

# 나쁜 프롬프트 예시
system_prompt = "작업을 해주세요."
```

### 2. 온도(Temperature) 조정
```python
# 창의적 작업: 높은 온도
config.temperature = 0.8

# 분석적 작업: 낮은 온도
config.temperature = 0.3

# 균형잡힌 작업: 중간 온도
config.temperature = 0.7
```

### 3. 토큰 수 관리
```python
# 긴 응답이 필요한 경우
config.max_tokens = 2000

# 간단한 응답만 필요한 경우
config.max_tokens = 500
```

## 비용 관리 (OpenAI)

### 토큰 사용량 모니터링
```python
class CostTracker:
    def __init__(self):
        self.total_tokens = 0
        self.total_cost = 0
    
    def track_usage(self, prompt_tokens, completion_tokens, model="gpt-3.5-turbo"):
        # GPT-3.5-turbo 가격 (2024년 기준)
        input_cost = prompt_tokens * 0.0015 / 1000
        output_cost = completion_tokens * 0.002 / 1000
        
        self.total_tokens += prompt_tokens + completion_tokens
        self.total_cost += input_cost + output_cost
        
        return input_cost + output_cost
```

### 비용 절약 팁
1. **적절한 모델 선택**: GPT-3.5-turbo vs GPT-4
2. **프롬프트 최적화**: 불필요한 내용 제거
3. **캐싱 활용**: 반복적인 요청 결과 저장
4. **배치 처리**: 여러 작업을 한 번에 처리

## 보안 고려사항

### API 키 보안
```python
# 환경 변수 사용 (권장)
import os
api_key = os.getenv("OPENAI_API_KEY")

# 하드코딩 금지
api_key = "sk-..." # 절대 하지 마세요!
```

### 데이터 보안
```python
# 민감한 정보 필터링
def sanitize_input(text):
    # 개인정보, 비밀번호 등 제거
    return filtered_text

# 로그 관리
logger.info("작업 실행")  # OK
logger.info(f"API 키: {api_key}")  # 절대 금지!
```

## 문제 해결

### 일반적인 오류들

#### 1. API 키 오류
```
Error: Invalid API key
```
**해결방법**: API 키 확인, 환경 변수 설정 확인

#### 2. 토큰 한도 초과
```
Error: Token limit exceeded
```
**해결방법**: max_tokens 조정, 프롬프트 길이 단축

#### 3. 네트워크 오류
```
Error: Connection timeout
```
**해결방법**: 인터넷 연결 확인, 재시도 로직 추가

#### 4. Ollama 연결 실패
```
Error: Ollama not running
```
**해결방법**: `ollama serve` 실행, 모델 다운로드 확인

## 실제 배포 시 고려사항

### 1. 환경 설정
```bash
# .env 파일
OPENAI_API_KEY=your-key-here
OLLAMA_BASE_URL=http://localhost:11434
LLM_PROVIDER=openai
LLM_MODEL=gpt-3.5-turbo
```

### 2. 에러 처리
```python
try:
    result = agent.execute_task(task)
except Exception as e:
    logger.error(f"Agent 실행 실패: {e}")
    # 폴백 로직 실행
    result = fallback_handler(task)
```

### 3. 모니터링
```python
# 성능 메트릭 수집
metrics = {
    "execution_time": result["execution_time"],
    "success_rate": calculate_success_rate(),
    "token_usage": track_token_usage(),
    "cost": calculate_cost()
}
```

## 다음 단계

1. **API 키 획득**: OpenAI 또는 다른 제공자에서 API 키 발급
2. **환경 설정**: 필요한 패키지 설치 및 설정
3. **테스트 실행**: 간단한 작업부터 시작
4. **성능 튜닝**: 프롬프트 및 파라미터 최적화
5. **프로덕션 배포**: 보안 및 모니터링 설정

실제 LLM을 연동하면 현재 시뮬레이션으로 보여드린 것보다 훨씬 더 지능적이고 창의적인 Agent를 경험할 수 있습니다!