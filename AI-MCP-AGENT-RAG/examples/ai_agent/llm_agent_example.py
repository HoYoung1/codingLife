"""
실제 LLM 기반 AI Agent 예제

진짜 추론 능력을 가진 Agent가 어떻게 동작하는지 시연합니다.
API 키가 없을 때는 시뮬레이션 모드로 동작하여 실제 LLM의 동작을 보여줍니다.
"""

import sys
import json
from pathlib import Path

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

from src.rag.rag_system import RAGSystem
from src.mcp.mcp_server import MCPServer, MCPTool
from src.mcp.tools.file_system_tools import FILE_SYSTEM_TOOLS
from src.mcp.tools.web_api_tools import WEB_API_TOOLS
from src.ai_agent.llm_agent import LLMAgent, LLMConfig, LLMProvider


def setup_systems():
    """RAG 시스템과 MCP 서버 설정"""
    print("🔧 시스템 초기화 중...")
    
    # 1. RAG 시스템 설정
    print("📚 RAG 시스템 초기화...")
    rag = RAGSystem(use_ollama=False)
    
    # Agent 가이드 문서 생성
    docs_dir = Path("llm_agent_knowledge")
    docs_dir.mkdir(exist_ok=True)
    
    llm_agent_guide = """# LLM Agent 작업 가이드

## 효과적인 작업 수행 방법

### 1. 상황 분석
- 사용자 요청을 정확히 이해하기
- 현재 상황과 목표 간의 차이 파악
- 필요한 정보와 도구 식별

### 2. 계획 수립
- 목표 달성을 위한 단계별 계획
- 각 단계에서 사용할 도구 선택
- 예상되는 결과와 대안 계획

### 3. 도구 활용 가이드

#### 파일 시스템 도구들
- list_files: 디렉토리 탐색, 파일 현황 파악
- read_file: 파일 내용 확인, 정보 수집
- write_file: 새 파일 생성, 내용 저장
- create_directory: 폴더 구조 생성
- get_file_info: 파일 상세 정보 조회

#### 정보 수집 도구들
- get_weather: 날씨 정보 조회
- get_news: 최신 뉴스 수집
- 정보는 사용자에게 유용한 형태로 가공하여 제공

#### 커뮤니케이션 도구들
- send_slack_message: 팀 커뮤니케이션
- get_slack_channels: 채널 정보 확인

### 4. 결과 분석 및 개선
- 각 단계의 성공/실패 분석
- 목표 달성도 평가
- 필요시 계획 수정 및 재실행

### 5. 효과적인 작업 패턴
- 정보 수집 → 분석 → 행동 → 검증 → 결과 제공
- 단계별 진행 상황 확인
- 사용자 요구사항에 맞는 결과 도출
"""
    
    with open(docs_dir / "llm_agent_guide.txt", "w", encoding="utf-8") as f:
        f.write(llm_agent_guide)
    
    # RAG에 문서 추가
    rag.add_documents([str(docs_dir / "llm_agent_guide.txt")])
    print("✅ RAG 시스템 초기화 완료")
    
    # 2. MCP 서버 설정
    print("🔧 MCP 서버 초기화...")
    server = MCPServer("LLM Agent MCP 서버")
    
    # 모든 도구 등록
    all_tools = FILE_SYSTEM_TOOLS + WEB_API_TOOLS
    for tool_config in all_tools:
        tool = MCPTool(
            name=tool_config["name"],
            description=tool_config["description"],
            parameters=tool_config["parameters"],
            function=tool_config["function"]
        )
        server.register_tool(tool)
    
    print(f"✅ MCP 서버 초기화 완료 ({len(all_tools)}개 도구)")
    
    return rag, server


def demonstrate_llm_vs_hardcoded():
    """LLM Agent vs 하드코딩 Agent 비교 시연"""
    print(f"\n{'='*80}")
    print("🧠 LLM Agent vs 📋 하드코딩 Agent 비교")
    print(f"{'='*80}")
    
    # 시스템 설정
    rag, mcp_server = setup_systems()
    
    # 1. 하드코딩 Agent (기존 구현)
    print("\n📋 하드코딩 Agent 동작:")
    print("- 미리 정의된 if-else 로직")
    print("- 예측 가능한 동작 패턴")
    print("- 제한적인 상황 대응")
    
    # 2. LLM Agent (새로운 구현)
    print("\n🧠 LLM Agent 동작:")
    print("- 실시간 상황 분석 및 추론")
    print("- 동적 계획 수립")
    print("- 창의적 문제 해결")
    
    # LLM Agent 생성
    llm_config = LLMConfig(
        provider=LLMProvider.SIMULATION,  # 시뮬레이션 모드
        model="gpt-3.5-turbo",
        temperature=0.7
    )
    
    llm_agent = LLMAgent(
        name="지능형 Assistant",
        llm_config=llm_config,
        rag_system=rag,
        mcp_server=mcp_server
    )
    
    return llm_agent


def run_llm_agent_scenarios(agent: LLMAgent):
    """다양한 시나리오로 LLM Agent 테스트"""
    
    scenarios = [
        {
            "name": "복잡한 정보 수집 작업",
            "description": "현재 프로젝트 상황을 파악하고, 서울 날씨와 최신 기술 뉴스를 조합해서 오늘의 작업 환경 리포트를 만들어주세요",
            "expected_behavior": "파일 탐색 → 날씨 조회 → 뉴스 수집 → 종합 분석 → 리포트 생성"
        },
        {
            "name": "창의적 문제 해결",
            "description": "팀 프로젝트 진행 상황을 정리하고 다음 주 계획을 세워주세요",
            "expected_behavior": "현재 상황 분석 → 진행 상황 파악 → 계획 수립 → 문서화"
        },
        {
            "name": "다단계 업무 처리",
            "description": "개발 환경을 점검하고 필요한 개선사항을 찾아서 액션 아이템을 만들어주세요",
            "expected_behavior": "환경 점검 → 문제점 식별 → 개선안 도출 → 액션 플랜 작성"
        }
    ]
    
    print(f"\n{'='*80}")
    print("🎯 LLM Agent 시나리오 테스트")
    print(f"{'='*80}")
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"\n🎬 시나리오 {i}: {scenario['name']}")
        print(f"📋 요청: {scenario['description']}")
        print(f"🎯 예상 동작: {scenario['expected_behavior']}")
        print(f"{'-'*60}")
        
        # LLM Agent 실행
        result = agent.execute_task(scenario['description'], max_steps=8)
        
        # 결과 분석
        print(f"\n📊 실행 결과:")
        print(f"   성공 여부: {'✅ 성공' if result['success'] else '❌ 실패'}")
        print(f"   실행 시간: {result.get('execution_time', 0):.2f}초")
        print(f"   총 단계 수: {result.get('total_steps', 0)}")
        
        if result.get('error'):
            print(f"   오류: {result['error']}")
        
        # 실행 과정 상세 분석
        print(f"\n🔍 실행 과정 분석:")
        
        thoughts = [h for h in result.get('history', []) if h['type'] == 'thought']
        actions = [h for h in result.get('history', []) if h['type'] == 'action']
        observations = [h for h in result.get('history', []) if h['type'] == 'observation']
        
        print(f"   🧠 사고 과정: {len(thoughts)}회")
        print(f"   🎬 행동 실행: {len(actions)}회")
        print(f"   👁️  결과 관찰: {len(observations)}회")
        
        # 주요 사고 과정 출력
        if thoughts:
            print(f"\n💭 주요 사고 과정:")
            for j, thought in enumerate(thoughts[:3], 1):
                print(f"   {j}. {thought['content'][:150]}...")
        
        # 실행한 도구들
        if actions:
            print(f"\n🛠️  사용한 도구들:")
            for action in actions:
                if isinstance(action['content'], dict) and 'tool_name' in action['content']:
                    tool_name = action['content']['tool_name']
                    success = "✅" if action['content'].get('success') else "❌"
                    print(f"   {success} {tool_name}")
        
        # 최종 요약
        if result.get('final_summary'):
            print(f"\n📝 최종 요약:")
            print(f"   {result['final_summary'][:200]}...")
        
        print(f"\n⏱️  시나리오 {i} 완료\n")


def interactive_llm_agent():
    """대화형 LLM Agent"""
    print(f"\n{'='*80}")
    print("💬 대화형 LLM Agent")
    print(f"{'='*80}")
    
    # 시스템 설정
    rag, mcp_server = setup_systems()
    
    # LLM Agent 생성
    llm_config = LLMConfig(
        provider=LLMProvider.SIMULATION,
        model="gpt-3.5-turbo",
        temperature=0.7
    )
    
    agent = LLMAgent(
        name="대화형 지능 Assistant",
        llm_config=llm_config,
        rag_system=rag,
        mcp_server=mcp_server
    )
    
    print("\n🤖 지능형 Agent와 대화해보세요!")
    print("💡 이 Agent는 실제 LLM처럼 상황을 분석하고 계획을 세웁니다.")
    print("\n예시 요청:")
    print("- '프로젝트 현황을 파악하고 주간 리포트를 만들어줘'")
    print("- '날씨 확인하고 오늘 일정에 맞는 조언을 해줘'")
    print("- '개발 환경을 점검하고 개선사항을 찾아줘'")
    print("- '팀에게 공유할 기술 뉴스 브리핑을 만들어줘'")
    print("\n종료하려면 'quit' 입력")
    
    while True:
        try:
            user_input = input(f"\n👤 사용자: ").strip()
            
            if user_input.lower() in ['quit', 'exit', '종료', 'q']:
                print("👋 대화를 종료합니다.")
                break
            
            if not user_input:
                continue
            
            print(f"\n🧠 Agent가 요청을 분석하고 있습니다...")
            
            # LLM Agent 실행
            result = agent.execute_task(user_input, max_steps=6)
            
            # 결과 출력
            if result['success']:
                print(f"\n✅ 작업 완료!")
                
                # 최종 요약 출력
                if result.get('final_summary'):
                    print(f"\n📋 결과 요약:")
                    print(f"{result['final_summary']}")
                
                # 실행 과정 간단히 출력
                thoughts = [h for h in result.get('history', []) if h['type'] == 'thought']
                actions = [h for h in result.get('history', []) if h['type'] == 'action']
                
                print(f"\n🔍 실행 과정: {len(thoughts)}단계 사고, {len(actions)}개 도구 사용")
                
            else:
                print(f"\n❌ 작업 처리 중 문제가 발생했습니다.")
                if result.get('error'):
                    print(f"오류: {result['error']}")
            
        except KeyboardInterrupt:
            print("\n\n👋 대화를 종료합니다.")
            break
        except Exception as e:
            print(f"❌ 오류 발생: {str(e)}")


def main():
    """메인 실행 함수"""
    print("=== 실제 LLM 기반 AI Agent 예제 ===")
    print("🧠 진짜 추론 능력을 가진 Agent의 동작을 시연합니다.")
    print("🎭 API 키가 없으므로 시뮬레이션 모드로 실제 LLM 동작을 모방합니다.\n")
    
    # LLM vs 하드코딩 비교
    llm_agent = demonstrate_llm_vs_hardcoded()
    
    # 시나리오 테스트
    run_llm_agent_scenarios(llm_agent)
    
    # 대화형 데모 선택
    print(f"\n{'='*80}")
    choice = input("대화형 LLM Agent를 체험해보시겠습니까? (y/n): ").strip().lower()
    
    if choice in ['y', 'yes', '예', 'ㅇ']:
        interactive_llm_agent()
    
    print(f"\n🎉 LLM Agent 예제 완료!")
    
    print(f"\n💡 핵심 차이점:")
    print("📋 하드코딩 Agent:")
    print("   - if문으로 고정된 로직")
    print("   - 예측 가능한 동작")
    print("   - 새로운 상황에 대응 어려움")
    
    print("\n🧠 LLM Agent:")
    print("   - 실시간 상황 분석 및 추론")
    print("   - 동적 계획 수립")
    print("   - 창의적 문제 해결")
    print("   - 자연어로 사고 과정 설명")
    
    print(f"\n🚀 실제 구현 시:")
    print("   - OpenAI API: config.provider = LLMProvider.OPENAI")
    print("   - Ollama: config.provider = LLMProvider.OLLAMA")
    print("   - API 키만 설정하면 진짜 LLM 연동!")
    
    print(f"\n🎯 이제 진짜 지능적인 Agent의 구조를 이해했습니다!")


if __name__ == "__main__":
    main()