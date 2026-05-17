#실습용 AOAI 환경변수 읽기
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent.parent / ".env")

AOAI_ENDPOINT=os.getenv("AOAI_ENDPOINT")
AOAI_API_KEY=os.getenv("AOAI_API_KEY")
AOAI_DEPLOY_GPT4O=os.getenv("AOAI_DEPLOY_GPT4O")
AOAI_DEPLOY_GPT4O_MINI=os.getenv("AOAI_DEPLOY_GPT4O_MINI")
AOAI_DEPLOY_EMBED_3_LARGE=os.getenv("AOAI_DEPLOY_EMBED_3_LARGE")
AOAI_DEPLOY_EMBED_3_SMALL=os.getenv("AOAI_DEPLOY_EMBED_3_SMALL")
AOAI_DEPLOY_EMBED_ADA=os.getenv("AOAI_DEPLOY_EMBED_ADA")


from openai import AzureOpenAI
import json
client = AzureOpenAI(
  azure_endpoint = AOAI_ENDPOINT,
  api_key=AOAI_API_KEY,
  api_version="2024-10-21"
)


# 1. 의도 분석 스키마 (enum 사용)
intent_schema = {
    "name": "intent_analysis_schema",
    "schema": {
        "type": "object",
        "properties": {
            "intent": {
                "type": "string",
                "enum": ["title_extraction", "article_summary", "sentiment_analysis", "general_conversation"]
            }
        },
        "required": ["intent"],
        "additionalProperties": False
    }
}

def analyze_intent(user_input: str) -> dict:
    """
    1. 사용자 의도 분석 함수
    사용자의 쿼리가 어떤 작업을 원하는지 분석합니다.
    """
    INTENT_SYSTEM_PROMPT = """당신은 사용자의 의도를 분석하는 AI입니다.
    사용자의 입력을 분석하여 다음 중 정확히 하나의 의도를 선택하세요:
    - title_extraction: 텍스트에서 제목을 찾아달라는 요청
    - article_summary: 긴 텍스트를 요약해달라는 요청
    - sentiment_analysis: 텍스트의 긍정/부정을 평가해달라는 요청
    - general_conversation: 위 작업과 관련 없는 일반적인 대화
    """

    response = client.chat.completions.create(
        model=AOAI_DEPLOY_GPT4O,
        messages=[
            {"role": "system", "content": INTENT_SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        response_format={
            "type": "json_schema",
            "json_schema": intent_schema,
        },
    )

    return json.loads(response.choices[0].message.content)


article = """
삼성전자가 차세대 3나노 GAA 공정 개발에 박차를 가하고 있다.
이번 공정은 기존 핀펫(FinFET) 방식 대비 전력 효율이 45% 향상되며,
성능은 23% 개선될 것으로 기대된다. 업계 전문가들은 이번 기술이
반도체 패권 경쟁에서 핵심 역할을 할 것으로 전망하고 있다.
"""

query = f"{article} 이 기사의 제목을 추출해줘."
print(analyze_intent(query))


# 2. 기사 제목 추출 스키마
title_extraction_schema = {}

def extract_title(user_input: str) -> dict:
    """
    2. 기사 제목 추출 함수
    텍스트에서 제목과 부제목을 추출합니다.
    """

    TITLE_SYSTEM_PROMPT = """당신은 텍스트에서 제목을 추출하는 전문가입니다.
    주어진 텍스트에서 주요 제목과 부제목을 찾아내세요.
    제목이 명확하지 않으면 텍스트의 핵심 주제를 제목으로 생성하세요.
    """

    response = client.chat.completions.create(
        model=AOAI_DEPLOY_GPT4O,
        messages=[
            {"role": "system", "content": TITLE_SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        response_format={
            "type": "json_schema",
            "json_schema": title_extraction_schema,
        },
    )

    return json.loads(response.choices[0].message.content)



# 3. 기사 본문 요약 스키마
summary_schema = {
    "name": "summary_schema",
    "schema": {
        "type": "object",
        "properties": {
            "summary": {"type": "string"},
            "key_points": {
                "type": "array",
                "items": {"type": "string"}
            },
            "word_count": {"type": "integer"}
        },
        "required": ["summary", "key_points", "word_count"],
        "additionalProperties": False
    }
}

def summarize_article(user_input: str) -> dict:
    """
    3. 기사 본문 요약 함수
    긴 텍스트를 핵심 포인트 중심으로 요약합니다.
    """

    SUMMARY_SYSTEM_PROMPT = """당신은 텍스트 요약 전문가입니다.
    주어진 텍스트를 간결하게 요약하고, 핵심 포인트를 3-5개로 추출하세요.
    요약문은 2-3문장으로 작성하세요.
    """
    response = client.chat.completions.create(
        model=AOAI_DEPLOY_GPT4O,
        messages=[
            {"role": "system", "content": SUMMARY_SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        response_format={
            "type": "json_schema",
            "json_schema": summary_schema,
        },
    )

    return json.loads(response.choices[0].message.content)


# 4. 기사 긍부정 평가 스키마
sentiment_schema = {
    "name": "sentiment_schema",
    "schema": {
        "type": "object",
        "properties": {
            "sentiment_label": {
                "type": "string",
                "enum": ["positive", "negative", "neutral"]
            },
            "reason": {"type": "string"}
        },
        "required": ["sentiment_label", "reason"],
        "additionalProperties": False
    }
}
def analyze_sentiment(user_input: str) -> dict:
    """
    4. 기사 긍부정 평가 함수
    텍스트의 감정을 분석하고 긍정/부정/중립을 판단합니다.
    """
    SENTIMENT_SYSTEM_PROMPT = """당신은 텍스트의 감정을 분석하는 전문가입니다.
    주어진 텍스트의 전반적인 톤을 분석하여:
    - positive: 긍정적 감정이 우세한 경우
    - negative: 부정적 감정이 우세한 경우
    - neutral: 중립적이거나 사실 전달만 하는 경우
    """
    response = client.chat.completions.create(
        model=AOAI_DEPLOY_GPT4O,
        messages=[
            {"role": "system", "content": SENTIMENT_SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        response_format={
            "type": "json_schema",
            "json_schema": sentiment_schema,
        },
    )

    return json.loads(response.choices[0].message.content)


# 5. 일반 대화 스키마
general_conversation_schema = {
    "name": "general_conversation_schema",
    "schema": {
        "type": "object",
        "properties": {
            "response": {"type": "string"},
            "is_question": {"type": "boolean"},
            "tone": {
                "type": "string",
                "enum": ["friendly", "professional", "casual", "formal"]
            }
        },
        "required": ["response", "is_question", "tone"],
        "additionalProperties": False
    }
}
def general_chat(user_input: str) -> dict:
    """
    5. 일반 대화 함수
    일반적인 대화에 응답합니다.
    """

    GENERAL_SYSTEM_PROMPT = """당신은 친근하고 도움이 되는 AI 어시스턴트입니다.
    사용자의 질문이나 대화에 자연스럽게 응답하세요.
    tone은 대화의 분위기에 맞게 선택하세요.
    """
    response = client.chat.completions.create(
        model=AOAI_DEPLOY_GPT4O,
        messages=[
            {"role": "system", "content": GENERAL_SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        response_format={
            "type": "json_schema",
            "json_schema": general_conversation_schema,
        },
    )

    return json.loads(response.choices[0].message.content)



# ============================================
# 메인 워크플로우 함수
# ============================================

def process_user_query(user_input: str):
    """
    사용자 쿼리를 받아 적절한 함수로 라우팅하여 처리하는 메인 워크플로우
    """
    print(f"\n{'='*60}")
    print(f"사용자 입력: {user_input}")
    print(f"{'='*60}\n")

    # Step 1: 의도 분석
    print("🔍 Step 1: 의도 분석 중...")
    intent_result = analyze_intent(user_input)
    intent = intent_result["intent"]
    print(f"분석 결과: {intent}\n")

    # Step 2: 의도에 따라 적절한 함수 호출
    if intent == "title_extraction":
        print("Step 2: 제목 추출 실행...")
        result = extract_title(user_input)
        print(f"결과: {json.dumps(result, ensure_ascii=False, indent=2)}")

    elif intent == "article_summary":
        print("Step 2: 본문 요약 실행...")
        result = summarize_article(user_input)
        print(f"결과: {json.dumps(result, ensure_ascii=False, indent=2)}")

    elif intent == "sentiment_analysis":
        print("Step 2: 감정 분석 실행...")
        result = analyze_sentiment(user_input)
        print(f"결과: {json.dumps(result, ensure_ascii=False, indent=2)}")

    elif intent == "general_conversation":
        print("Step 2: 일반 대화 처리 중...")
        result = general_chat(user_input)
        print(f"결과: {json.dumps(result, ensure_ascii=False, indent=2)}")

    else:
        print("의도를 파악할 수 없습니다.")
        result = None



user = f"""
이 기사가 긍정적으로 쓰였나?
{article}
"""
process_user_query(user)
