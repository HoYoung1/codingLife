"""
RAG 인덱싱 스크립트.
최초 1회 또는 data/ 변경 시 실행: python -m backend.rag.ingest
"""

from pathlib import Path

from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter

from backend.config import get_embeddings, LLM_PROVIDER

load_dotenv()

DATA_DIR = Path(__file__).parent.parent.parent / "data"
INDEX_DIR = Path(__file__).parent / "faiss_index"


def build_index() -> None:
    print(f"[ingest] 데이터 로드: {DATA_DIR}  (provider: {LLM_PROVIDER})")
    loader = DirectoryLoader(
        str(DATA_DIR),
        glob="**/*.txt",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
    )
    docs = loader.load()
    print(f"[ingest] 문서 {len(docs)}개 로드 완료")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=80,
        separators=["\n\n", "\n", "。", ". ", " "],
    )
    chunks = splitter.split_documents(docs)
    print(f"[ingest] 청크 {len(chunks)}개 생성")

    # Azure 임베딩 rate limit 방어: 배치 사이 대기
    if LLM_PROVIDER == "azure":
        import time
        embeddings = get_embeddings()
        all_chunks = []
        batch_size = 10
        for i in range(0, len(chunks), batch_size):
            all_chunks.extend(chunks[i:i + batch_size])
            if i + batch_size < len(chunks):
                time.sleep(1)
        chunks = all_chunks

    print(f"[ingest] 임베딩 생성 중...")
    embeddings = get_embeddings()
    db = FAISS.from_documents(chunks, embeddings)
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    db.save_local(str(INDEX_DIR))
    print(f"[ingest] FAISS 인덱스 저장 완료: {INDEX_DIR}")


if __name__ == "__main__":
    build_index()
