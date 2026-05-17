import os
from pathlib import Path
from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config.settings import (
    AOAI_ENDPOINT, AOAI_API_KEY, AOAI_DEPLOY_EMBED_3_SMALL,
    AOAI_API_VERSION, CONTRACTS_DIR, VECTOR_STORE_DIR
)

_vector_store = None


def _get_embeddings():
    return AzureOpenAIEmbeddings(
        azure_endpoint=AOAI_ENDPOINT,
        api_key=AOAI_API_KEY,
        azure_deployment=AOAI_DEPLOY_EMBED_3_SMALL,
        api_version=AOAI_API_VERSION,
    )


def build_vector_store() -> FAISS:
    docs = []
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    for txt_file in Path(CONTRACTS_DIR).glob("*.txt"):
        loader = TextLoader(str(txt_file), encoding="utf-8")
        raw = loader.load()
        chunks = splitter.split_documents(raw)
        for chunk in chunks:
            chunk.metadata["source"] = txt_file.stem
        docs.extend(chunks)

    store = FAISS.from_documents(docs, _get_embeddings())
    VECTOR_STORE_DIR.mkdir(exist_ok=True)
    store.save_local(str(VECTOR_STORE_DIR))
    return store


def get_vector_store() -> FAISS:
    global _vector_store
    if _vector_store is not None:
        return _vector_store

    if Path(VECTOR_STORE_DIR).exists() and any(Path(VECTOR_STORE_DIR).iterdir()):
        _vector_store = FAISS.load_local(
            str(VECTOR_STORE_DIR),
            _get_embeddings(),
            allow_dangerous_deserialization=True,
        )
    else:
        _vector_store = build_vector_store()
    return _vector_store


def search_contracts(query: str, k: int = 4) -> str:
    store = get_vector_store()
    results = store.similarity_search(query, k=k)
    if not results:
        return "관련 계약 정보를 찾을 수 없습니다."
    return "\n\n---\n\n".join(
        f"[출처: {doc.metadata.get('source', '알 수 없음')}]\n{doc.page_content}"
        for doc in results
    )
