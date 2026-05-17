"""
LLM_PROVIDER=ollama  → 로컬 Ollama 사용
LLM_PROVIDER=azure   → Azure OpenAI 사용 (사내망/운영 환경)
"""

import os
from dotenv import load_dotenv

load_dotenv()

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama").lower()


def get_llm(large: bool = False, json_mode: bool = False):
    """
    large=True  : 고품질 모델 (Strategist 전용) — Azure: gpt-4o / Ollama: 동일 모델
    json_mode=True : JSON 출력 강제
    """
    if LLM_PROVIDER == "azure":
        from langchain_openai import AzureChatOpenAI
        deploy = (
            os.environ["AOAI_DEPLOY_GPT4O"] if large
            else os.environ["AOAI_DEPLOY_GPT4O_MINI"]
        )
        kwargs = {}
        if json_mode:
            kwargs["model_kwargs"] = {"response_format": {"type": "json_object"}}
        return AzureChatOpenAI(
            azure_endpoint=os.environ["AOAI_ENDPOINT"],
            api_key=os.environ["AOAI_API_KEY"],
            azure_deployment=deploy,
            api_version="2024-02-01",
            temperature=0,
            **kwargs,
        )
    else:
        from langchain_ollama import ChatOllama
        kwargs = {}
        if json_mode:
            kwargs["format"] = "json"
        return ChatOllama(
            model=os.getenv("OLLAMA_MODEL", "llama3.1:8b"),
            base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
            temperature=0,
            **kwargs,
        )


def get_embeddings():
    if LLM_PROVIDER == "azure":
        from langchain_openai import AzureOpenAIEmbeddings
        return AzureOpenAIEmbeddings(
            azure_endpoint=os.environ["AOAI_ENDPOINT"],
            api_key=os.environ["AOAI_API_KEY"],
            azure_deployment=os.environ["AOAI_DEPLOY_EMBED_3_SMALL"],
            api_version="2024-02-01",
        )
    else:
        from langchain_ollama import OllamaEmbeddings
        return OllamaEmbeddings(
            model=os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text"),
            base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        )
