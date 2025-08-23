"""
RAG 시스템 사용 예제
"""

import os
import sys
from pathlib import Path

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from src.rag_system import RAGSystem


def create_sample_documents():
    """테스트용 샘플 문서 생성"""
    docs_dir = Path("sample_docs")
    docs_dir.mkdir(exist_ok=True)
    
    # 샘플 문서 1: AI 기술 소개
    ai_intro = """인공지능(AI) 기술의 발전

인공지능은 컴퓨터가 인간의 지능을 모방하여 학습하고 추론할 수 있도록 하는 기술입니다.

주요 AI 기술들:
1. 머신러닝: 데이터로부터 패턴을 학습하여 예측하는 기술
2. 딥러닝: 신경망을 사용하여 복잡한 패턴을 학습하는 기술
3. 자연어처리: 인간의 언어를 이해하고 생성하는 기술

AI의 응용 분야:
- 자율주행차
- 의료 진단
- 금융 분석
- 고객 서비스
- 교육

AI 기술의 장점:
- 24시간 작업 가능
- 대량 데이터 처리
- 일관된 성능
- 위험한 환경에서 작업 가능

AI 기술의 한계:
- 창의성 부족
- 윤리적 판단 어려움
- 데이터 의존성
- 설명 가능성 부족"""
    
    with open(docs_dir / "ai_introduction.txt", "w", encoding="utf-8") as f:
        f.write(ai_intro)
    
    # 샘플 문서 2: RAG 시스템 설명
    rag_explanation = """RAG (Retrieval-Augmented Generation) 시스템

RAG는 검색 기반 생성 시스템으로, 대규모 언어 모델이 외부 지식 베이스에서 정보를 검색하여 
더 정확하고 최신 정보를 바탕으로 응답을 생성하는 기술입니다.

RAG 시스템의 구성 요소:
1. 문서 처리기: 다양한 형식의 문서를 텍스트로 변환하고 청킹
2. 임베딩 생성기: 텍스트를 벡터로 변환
3. 벡터 데이터베이스: 임베딩을 저장하고 유사도 검색 수행
4. 생성 모델: 검색된 정보를 바탕으로 응답 생성

RAG의 장점:
- 최신 정보 활용 가능
- 검증된 문서 기반 응답
- 응답 출처 추적 가능
- 다양한 도메인 지원

RAG의 활용 사례:
- 고객 지원 시스템
- 교육 플랫폼
- 연구 도구
- 문서 검색 시스템"""
    
    with open(docs_dir / "rag_explanation.txt", "w", encoding="utf-8") as f:
        f.write(rag_explanation)
    
    # 샘플 문서 3: MCP 프로토콜 소개
    mcp_intro = """MCP (Model Context Protocol) 프로토콜

MCP는 AI 모델과 외부 도구 및 서비스를 연결하는 표준 프로토콜입니다.

MCP의 핵심 개념:
1. 도구 호출: AI가 외부 도구를 호출하여 작업 수행
2. 함수 정의: 도구의 기능을 명확하게 정의
3. 컨텍스트 관리: AI와 도구 간의 상태 정보 공유
4. 보안: 안전한 도구 호출 및 권한 관리

MCP의 장점:
- 모듈화된 AI 시스템 구축
- 기존 도구와의 통합 용이
- 확장 가능한 AI 기능
- 표준화된 인터페이스

MCP 활용 예시:
- 파일 시스템 접근
- 데이터베이스 쿼리
- 웹 API 호출
- 외부 서비스 연동"""
    
    with open(docs_dir / "mcp_protocol.txt", "w", encoding="utf-8") as f:
        f.write(mcp_intro)
    
    print("샘플 문서가 생성되었습니다:")
    for doc in docs_dir.glob("*.txt"):
        print(f"  - {doc.name}")
    
    return [str(doc) for doc in docs_dir.glob("*.txt")]


def main():
    """메인 실행 함수"""
    print("=== RAG 시스템 테스트 (로컬 모델 사용) ===\n")
    
    print("🔍 시스템 초기화 중...")
    print("📝 Sentence Transformers를 사용하여 로컬에서 임베딩을 생성합니다.")
    print("🤖 Ollama가 설치되어 있다면 LLM 모드로, 없다면 키워드 매칭 모드로 작동합니다.\n")
    
    # RAG 시스템 초기화 (Ollama 사용 시도)
    try:
        rag = RAGSystem(use_ollama=True, ollama_model="llama2")
        print("✅ RAG 시스템 초기화 완료!")
        print("💡 Ollama가 연결되었습니다. 고품질 LLM 기반 답변을 생성합니다.")
    except Exception as e:
        print(f"⚠️  Ollama 연결 실패: {e}")
        print("🔍 키워드 매칭 모드로 전환합니다.")
        rag = RAGSystem(use_ollama=False)
        print("✅ 키워드 매칭 모드로 RAG 시스템 초기화 완료!")
    
    # 샘플 문서 생성
    print("\n📚 샘플 문서 생성 중...")
    sample_files = create_sample_documents()
    
    # 문서 추가
    print("\n📖 문서를 RAG 시스템에 추가 중...")
    success = rag.add_documents(sample_files)
    
    if not success:
        print("❌ 문서 추가에 실패했습니다.")
        return
    
    print("✅ 문서 추가 완료!")
    
    # 시스템 정보 확인
    info = rag.get_document_info()
    print(f"\n📊 시스템 정보: {info['total_documents']}개 문서가 로드되었습니다.")
    
    # 질의응답 테스트
    print("\n🔍 질의응답 테스트를 시작합니다...")
    
    test_questions = [
        "AI 기술의 주요 장점은 무엇인가요?",
        "RAG 시스템이란 무엇이며 어떻게 작동하나요?",
        "MCP 프로토콜의 핵심 개념은 무엇인가요?",
        "머신러닝과 딥러닝의 차이점은 무엇인가요?"
    ]
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n--- 질문 {i} ---")
        print(f"Q: {question}")
        
        try:
            result = rag.query(question)
            print(f"A: {result['answer']}")
            
            if result['relevant_documents']:
                print("\n관련 문서:")
                for j, doc in enumerate(result['relevant_documents'], 1):
                    print(f"  {j}. {doc['content']}")
                    
        except Exception as e:
            print(f"❌ 오류 발생: {str(e)}")
    
    print("\n🎉 RAG 시스템 테스트가 완료되었습니다!")
    print("\n💡 시스템 정보:")
    print("- 임베딩: Sentence Transformers (all-MiniLM-L6-v2)")
    print("- 벡터 DB: ChromaDB")
    print("- LLM: Ollama (설치된 경우) 또는 키워드 매칭")
    
    print("\n🚀 다음 단계:")
    print("1. 웹 인터페이스 실행: python -m uvicorn src.web_interface:app --reload")
    print("2. 더 많은 문서 추가")
    print("3. Ollama 설치하여 LLM 모드 사용")
    print("4. 프롬프트 템플릿 커스터마이징")


if __name__ == "__main__":
    main()
