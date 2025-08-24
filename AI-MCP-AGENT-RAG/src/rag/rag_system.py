"""
RAG (Retrieval-Augmented Generation) 시스템 구현
"""

import os
from typing import List, Dict, Any
from pathlib import Path
import logging

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import (
    TextLoader, 
    PyPDFLoader, 
    Docx2txtLoader,
    UnstructuredMarkdownLoader
)
from langchain.schema import Document
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DocumentProcessor:
    """문서 처리 및 청킹을 담당하는 클래스"""
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
        )
    
    def load_document(self, file_path: str) -> List[Document]:
        """다양한 형식의 문서를 로드하고 텍스트로 변환"""
        file_path = Path(file_path)
        
        try:
            if file_path.suffix.lower() == '.txt':
                loader = TextLoader(str(file_path), encoding='utf-8')
            elif file_path.suffix.lower() == '.pdf':
                loader = PyPDFLoader(str(file_path))
            elif file_path.suffix.lower() == '.docx':
                loader = Docx2txtLoader(str(file_path))
            elif file_path.suffix.lower() == '.md':
                loader = UnstructuredMarkdownLoader(str(file_path))
            else:
                raise ValueError(f"지원하지 않는 파일 형식: {file_path.suffix}")
            
            documents = loader.load()
            logger.info(f"문서 로드 완료: {file_path.name} ({len(documents)} 페이지)")
            return documents
            
        except Exception as e:
            logger.error(f"문서 로드 실패: {file_path.name} - {str(e)}")
            return []
    
    def chunk_documents(self, documents: List[Document]) -> List[Document]:
        """문서를 청크로 분할"""
        try:
            chunks = self.text_splitter.split_documents(documents)
            logger.info(f"문서 청킹 완료: {len(chunks)}개 청크 생성")
            return chunks
        except Exception as e:
            logger.error(f"문서 청킹 실패: {str(e)}")
            return []


class VectorStore:
    """벡터 저장소 관리 클래스"""
    
    def __init__(self, persist_directory: str = "./chroma_db"):
        self.persist_directory = persist_directory
        # 로컬 임베딩 모델 사용 (OpenAI 대신)
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'},  # GPU가 있다면 'cuda'로 변경 가능
            encode_kwargs={'normalize_embeddings': True}
        )
        self.vectorstore = None
    
    def create_vectorstore(self, documents: List[Document]) -> Chroma:
        """문서로부터 벡터 저장소 생성"""
        try:
            self.vectorstore = Chroma.from_documents(
                documents=documents,
                embedding=self.embeddings,
                persist_directory=self.persist_directory
            )
            self.vectorstore.persist()
            logger.info(f"벡터 저장소 생성 완료: {self.persist_directory}")
            return self.vectorstore
        except Exception as e:
            logger.error(f"벡터 저장소 생성 실패: {str(e)}")
            raise
    
    def load_vectorstore(self) -> Chroma:
        """기존 벡터 저장소 로드"""
        try:
            self.vectorstore = Chroma(
                persist_directory=self.persist_directory,
                embedding_function=self.embeddings
            )
            logger.info("기존 벡터 저장소 로드 완료")
            return self.vectorstore
        except Exception as e:
            logger.error(f"벡터 저장소 로드 실패: {str(e)}")
            raise
    
    def similarity_search(self, query: str, k: int = 4) -> List[Document]:
        """유사도 검색 수행"""
        if not self.vectorstore:
            raise ValueError("벡터 저장소가 초기화되지 않았습니다.")
        
        try:
            results = self.vectorstore.similarity_search(query, k=k)
            logger.info(f"검색 완료: '{query}' -> {len(results)}개 결과")
            return results
        except Exception as e:
            logger.error(f"검색 실패: {str(e)}")
            return []


class RAGSystem:
    """RAG 시스템 메인 클래스"""
    
    def __init__(self, use_ollama: bool = True, ollama_model: str = "llama2"):
        self.document_processor = DocumentProcessor()
        self.vector_store = VectorStore()
        
        # LLM 설정 - Ollama 사용 (로컬에서 실행)
        if use_ollama:
            try:
                self.llm = Ollama(model=ollama_model)
                logger.info(f"Ollama 모델 '{ollama_model}' 사용")
            except Exception as e:
                logger.warning(f"Ollama 연결 실패: {e}. 간단한 키워드 매칭 모드로 전환합니다.")
                self.llm = None
        else:
            self.llm = None
        
        self.qa_chain = None
    
    def add_documents(self, file_paths: List[str]) -> bool:
        """문서를 시스템에 추가"""
        try:
            all_documents = []
            
            for file_path in file_paths:
                documents = self.document_processor.load_document(file_path)
                if documents:
                    all_documents.extend(documents)
            
            if not all_documents:
                logger.warning("추가할 문서가 없습니다.")
                return False
            
            # 문서 청킹
            chunks = self.document_processor.chunk_documents(all_documents)
            
            # 벡터 저장소 생성 또는 업데이트
            if self.vector_store.vectorstore:
                # 기존 저장소에 추가
                self.vector_store.vectorstore.add_documents(chunks)
                self.vector_store.vectorstore.persist()
                logger.info("기존 벡터 저장소에 문서 추가 완료")
            else:
                # 새 저장소 생성
                self.vector_store.create_vectorstore(chunks)
            
            # QA 체인 재생성
            self._create_qa_chain()
            return True
            
        except Exception as e:
            logger.error(f"문서 추가 실패: {str(e)}")
            return False
    
    def _create_qa_chain(self):
        """QA 체인 생성"""
        try:
            if self.llm:
                # LLM이 있는 경우 LangChain 체인 사용
                prompt_template = """다음 컨텍스트를 사용하여 질문에 답변하세요:

컨텍스트:
{context}

질문: {question}

답변:"""
                
                prompt = PromptTemplate(
                    template=prompt_template,
                    input_variables=["context", "question"]
                )
                
                self.qa_chain = RetrievalQA.from_chain_type(
                    llm=self.llm,
                    chain_type="stuff",
                    retriever=self.vector_store.vectorstore.as_retriever(search_kwargs={"k": 4}),
                    chain_type_kwargs={"prompt": prompt}
                )
                
                logger.info("LLM 기반 QA 체인 생성 완료")
            else:
                # LLM이 없는 경우 간단한 키워드 매칭 모드
                logger.info("간단한 키워드 매칭 모드로 QA 체인 생성")
                self.qa_chain = "keyword_matching"
            
        except Exception as e:
            logger.error(f"QA 체인 생성 실패: {str(e)}")
    
    def query(self, question: str) -> Dict[str, Any]:
        """질문에 대한 답변 생성"""
        try:
            if not self.qa_chain:
                raise ValueError("QA 체인이 초기화되지 않았습니다.")
            
            # 유사한 문서 검색
            relevant_docs = self.vector_store.similarity_search(question, k=4)
            
            if not relevant_docs:
                return {
                    "question": question,
                    "answer": "관련된 문서를 찾을 수 없습니다.",
                    "relevant_documents": []
                }
            
            if self.qa_chain == "keyword_matching":
                # 간단한 키워드 매칭 모드
                answer = self._simple_keyword_answer(question, relevant_docs)
            else:
                # LLM 기반 답변 생성
                result = self.qa_chain({"query": question})
                answer = result["result"]
            
            return {
                "question": question,
                "answer": answer,
                "relevant_documents": [
                    {
                        "content": doc.page_content[:200] + "...",
                        "metadata": doc.metadata
                    }
                    for doc in relevant_docs
                ]
            }
            
        except Exception as e:
            logger.error(f"질의응답 실패: {str(e)}")
            return {
                "question": question,
                "answer": f"오류가 발생했습니다: {str(e)}",
                "relevant_documents": []
            }
    
    def _simple_keyword_answer(self, question: str, relevant_docs: List[Document]) -> str:
        """간단한 키워드 기반 답변 생성"""
        # 질문에서 주요 키워드 추출
        question_words = set(question.lower().split())
        
        # 가장 관련성 높은 문서 찾기
        best_doc = None
        best_score = 0
        
        for doc in relevant_docs:
            doc_words = set(doc.page_content.lower().split())
            # 단어 겹침으로 관련성 계산
            overlap = len(question_words.intersection(doc_words))
            if overlap > best_score:
                best_score = overlap
                best_doc = doc
        
        if best_doc:
            # 관련 문장들을 추출하여 답변 생성
            sentences = best_doc.page_content.split('.')
            relevant_sentences = []
            
            for sentence in sentences:
                sentence_lower = sentence.lower()
                if any(word in sentence_lower for word in question_words):
                    relevant_sentences.append(sentence.strip())
            
            if relevant_sentences:
                answer = " ".join(relevant_sentences[:3]) + "."
                return answer
        
        # 기본 답변
        return f"검색된 문서에서 '{question}'과 관련된 정보를 찾았습니다. 자세한 내용은 관련 문서를 참조하세요."
    
    def get_document_info(self) -> Dict[str, Any]:
        """현재 시스템의 문서 정보 반환"""
        if not self.vector_store.vectorstore:
            return {"total_documents": 0, "collection_info": None}
        
        try:
            collection = self.vector_store.vectorstore._collection
            count = collection.count()
            
            return {
                "total_documents": count,
                "collection_info": {
                    "name": collection.name,
                    "metadata": collection.metadata
                }
            }
        except Exception as e:
            logger.error(f"문서 정보 조회 실패: {str(e)}")
            return {"total_documents": 0, "collection_info": None}


# 사용 예시
if __name__ == "__main__":
    # RAG 시스템 초기화 (Ollama 사용)
    rag = RAGSystem(use_ollama=True, ollama_model="llama2")
    
    # 샘플 문서 추가 (실제 파일 경로로 변경 필요)
    # sample_files = ["sample1.txt", "sample2.pdf"]
    # rag.add_documents(sample_files)
    
    print("RAG 시스템이 준비되었습니다!")
    print("문서를 추가하려면 add_documents() 메서드를 사용하세요.")
    print("질문하려면 query() 메서드를 사용하세요.")
    print("\n참고: Ollama가 설치되어 있지 않다면 간단한 키워드 매칭 모드로 작동합니다.")
