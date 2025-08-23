#!/usr/bin/env python3
"""
RAG 시스템 실행 스크립트 (로컬 모델 사용)
"""

import os
import sys
from pathlib import Path

def main():
    """메인 실행 함수"""
    print("🤖 RAG 시스템 시작 (로컬 모델 사용)")
    print("=" * 60)
    
    print("💡 이 시스템은 OpenAI API 키 없이도 작동합니다!")
    print("📝 Sentence Transformers를 사용하여 로컬에서 임베딩을 생성합니다.")
    print("🤖 Ollama가 설치되어 있다면 고품질 LLM 답변도 가능합니다.\n")
    
    # 실행 모드 선택
    print("실행 모드를 선택하세요:")
    print("1. 콘솔 모드 (예제 실행)")
    print("2. 웹 인터페이스")
    print("3. 종료")
    
    while True:
        choice = input("\n선택 (1-3): ").strip()
        
        if choice == "1":
            run_console_mode()
            break
        elif choice == "2":
            run_web_interface()
            break
        elif choice == "3":
            print("👋 프로그램을 종료합니다.")
            break
        else:
            print("❌ 잘못된 선택입니다. 1-3 중에서 선택해주세요.")


def run_console_mode():
    """콘솔 모드 실행"""
    print("\n📚 콘솔 모드로 RAG 시스템을 실행합니다...")
    
    try:
        # 예제 스크립트 실행
        from examples.rag_example import main as run_example
        run_example()
        
    except ImportError as e:
        print(f"❌ 예제 모듈을 불러올 수 없습니다: {e}")
        print("requirements.txt의 패키지들이 설치되었는지 확인해주세요.")
    except Exception as e:
        print(f"❌ 콘솔 모드 실행 중 오류 발생: {e}")


def run_web_interface():
    """웹 인터페이스 실행"""
    print("\n🌐 웹 인터페이스를 시작합니다...")
    
    try:
        import uvicorn
        from src.web_interface import app
        
        print("✅ 웹 서버를 시작합니다...")
        print("🌐 브라우저에서 http://localhost:8000 으로 접속하세요.")
        print("⏹️  서버를 중지하려면 Ctrl+C를 누르세요.")
        print("\n💡 시스템 정보:")
        print("- 임베딩: Sentence Transformers (all-MiniLM-L6-v2)")
        print("- 벡터 DB: ChromaDB")
        print("- LLM: Ollama (설치된 경우) 또는 키워드 매칭")
        
        uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
        
    except ImportError as e:
        print(f"❌ 필요한 패키지가 설치되지 않았습니다: {e}")
        print("다음 명령어로 패키지를 설치해주세요:")
        print("pip install -r requirements.txt")
    except Exception as e:
        print(f"❌ 웹 인터페이스 실행 중 오류 발생: {e}")


def check_dependencies():
    """의존성 패키지 확인"""
    print("\n🔍 의존성 패키지 확인 중...")
    
    required_packages = [
        "langchain",
        "langchain-community",
        "sentence-transformers",
        "torch",
        "transformers",
        "chromadb",
        "fastapi",
        "uvicorn"
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace("-", "_"))
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package}")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n❌ 다음 패키지들이 설치되지 않았습니다: {', '.join(missing_packages)}")
        print("다음 명령어로 설치해주세요:")
        print("pip install -r requirements.txt")
        return False
    
    print("\n✅ 모든 의존성 패키지가 설치되었습니다.")
    return True


def show_system_info():
    """시스템 정보 표시"""
    print("\n💡 시스템 구성:")
    print("📝 임베딩 모델: Sentence Transformers (all-MiniLM-L6-v2)")
    print("🗄️  벡터 데이터베이스: ChromaDB")
    print("🤖 LLM 옵션:")
    print("   - Ollama (설치된 경우): 고품질 LLM 답변")
    print("   - 키워드 매칭 (기본): 간단한 키워드 기반 답변")
    print("\n🚀 Ollama 설치 (선택사항):")
    print("   - macOS: brew install ollama")
    print("   - Linux: curl -fsSL https://ollama.ai/install.sh | sh")
    print("   - Windows: https://ollama.ai/download")
    print("   - 설치 후: ollama pull llama2")


if __name__ == "__main__":
    # 의존성 확인
    if not check_dependencies():
        sys.exit(1)
    
    # 시스템 정보 표시
    show_system_info()
    
    # 메인 실행
    main()
