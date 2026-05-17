from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS

from backend.config import get_embeddings

load_dotenv()

INDEX_DIR = Path(__file__).parent / "faiss_index"


@lru_cache(maxsize=1)
def _load_db() -> FAISS:
    return FAISS.load_local(
        str(INDEX_DIR),
        get_embeddings(),
        allow_dangerous_deserialization=True,  # 신뢰할 수 있는 로컬 인덱스
    )


def retrieve_context(query: str, k: int = 4) -> str:
    db = _load_db()
    docs = db.similarity_search(query, k=k)
    return "\n\n---\n\n".join(
        f"[출처: {Path(d.metadata.get('source', 'unknown')).name}]\n{d.page_content}"
        for d in docs
    )


def index_exists() -> bool:
    return (INDEX_DIR / "index.faiss").exists()
