"""
간단한 시뮬레이션 Agent 예제

외부 라이브러리 의존성 없이 순수 Python으로 구현한 Agent입니다.
실제 LLM의 추론 과정을 시뮬레이션하여 보여줍니다.
"""

import sys
import json
from pathlib import Path

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

from src.mcp.mcp_server import MCPServer, MCPTool
from src.mcp.tools.file_system_tools import FILE_SYSTEM_TOOLS
from src.mcp.tools.web_api_tools import WEB_API_TOOLS
from src.ai_agent.simple_agent import SimpleAgent


def setup_mcp_server():
    """MCP 서버 설정"""
    print("🔧 MCP 서버 초기화 중...")
    
    server = MCPServer("Simple Agent MCP 서버")
    
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
    return server


def demonstrate_agent_scenarios():
    """다양한 Agent 시나리오 시연"""
    
    # MCP 서버 설정
    mcp_server = setup_mcp_server()
    
    # Simple Agent 생성
    print("\n🤖 Simple Agent 생성 중...")
    agent = SimpleAgent("지능형 시뮬레이션 Assistant", mcp_server)
    
    # 테스트 시나리오들
    scenarios = [
        {
            "name": "파일 시스템 탐색",
            "description": "현재 디렉토리의 파일들을 조사하고 정리해주세요",
            "max_steps": 4
        },
        {
            "name": "날씨 정보 수집",
            "description": "서울의 현재 날씨를 확인해주세요",
            "max_steps": 3
        },
        {
            "name": "종합 정보 리포트",
            "description": "날씨와 뉴스를 조합해서 오늘의 브리핑 리포트를 만들어주세요",
            "max_steps": 6
        },
        {
            "name": "프로젝트 분석",
            "description": "현재 프로젝트 상황을 분석하고 개선사항을 제안해주세요",
            "max_steps": 5
        }
    ]
    
    print(f"\n{'='*80}")
    print("🎯 Simple Agent 시나리오 테스트")
    print(f"{'='*80}")
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"\n🎬 시나리오 {i}: {scenario['name']}")
        print(f"📋 요청: {scenario['description']}")
        print(f"{'-'*60}")
        
        # Agent 실행
        result = agent.execute_task(scenario['description'], scenario['max_steps'])
        
        # 결과 분석
        print(f"\n📊 실행 결과:")
        print(f"   성공 여부: {'✅ 성공' if result['success'] else '❌ 실패'}")
        print(f"   실행 시간: {result.get('execution_time', 0):.2f}초")
        print(f"   총 단계 수: {result.get('total_steps', 0)}")
        
        if result.get('error'):
            print(f"   오류: {result['error']}")
        
        # 실행 과정 요약
        history = result.get('history', [])
        thoughts = [h for h in history if h['type'] == 'thought']
        actions = [h for h in history if h['type'] == 'action']
        observations = [h for h in history if h['type'] == 'observation']
        
        print(f"\n🔍 실행 과정:")
        print(f"   🧠 사고 과정: {len(thoughts)}회")
        print(f"   🎬 행동 실행: {len(actions)}회")
        print(f"   👁️  결과 관찰: {len(observations)}회")
        
        # 주요 사고 과정 출력
        if thoughts:
            print(f"\n💭 주요 사고 과정:")
            for j, thought in enumerate(thoughts[:2], 1):
                print(f"   {j}. {thought['content'][:120]}...")
        
        # 사용한 도구들
        if actions:
            print(f"\n🛠️  사용한 도구들:")
            for action in actions:
                try:
                    action_data = json.loads(action['content'])
                    tool_name = action_data.get('tool_name', 'unknown')
                    success = "✅" if action_data.get('success') else "❌"
                    print(f"   {success} {tool_name}")
                except:
                    print(f"   🔧 도구 실행")
        
        # 최종 요약
        if result.get('final_summary'):
            print(f"\n📝 최종 요약:")
            print(f"   {result['final_summary'][:150]}...")
        
        print(f"\n⏱️  시나리오 {i} 완료\n")


def interactive_simple_agent():
    """대화형 Simple Agent"""
    print(f"\n{'='*80}")
    print("💬 대화형 Simple Agent")
    print(f"{'='*80}")
    
    # MCP 서버 설정
    mcp_server = setup_mcp_server()
    
    # Agent 생성
    agent = SimpleAgent("대화형 Assistant", mcp_server)
    
    print("\n🤖 Simple Agent와 대화해보세요!")
    print("💡 이 Agent는 실제 추론 과정을 시뮬레이션합니다.")
    print("\n예시 요청:")
    print("- '현재 디렉토리 파일들을 확인해줘'")
    print("- '서울 날씨를 알려줘'")
    print("- '최신 뉴스를 확인해줘'")
    print("- '프로젝트 리포트를 만들어줘'")
    print("- '팀에게 작업 완료 메시지를 보내줘'")
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
            
            # Agent 실행
            result = agent.execute_task(user_input, max_steps=5)
            
            # 결과 출력
            if result['success']:
                print(f"\n✅ 작업 완료!")
                
                # 최종 요약 출력
                if result.get('final_summary'):
                    print(f"\n📋 결과:")
                    print(f"{result['final_summary']}")
                
                # 실행 통계
                history = result.get('history', [])
                thoughts = len([h for h in history if h['type'] == 'thought'])
                actions = len([h for h in history if h['type'] == 'action'])
                
                print(f"\n📊 실행 통계: {thoughts}단계 사고, {actions}개 도구 사용")
                
            else:
                print(f"\n❌ 작업 처리 중 문제가 발생했습니다.")
                if result.get('error'):
                    print(f"오류: {result['error']}")
            
        except KeyboardInterrupt:
            print("\n\n👋 대화를 종료합니다.")
            break
        except Exception as e:
            print(f"❌ 오류 발생: {str(e)}")


def compare_agent_types():
    """Agent 유형별 비교"""
    print(f"\n{'='*80}")
    print("🔍 Agent 유형별 비교")
    print(f"{'='*80}")
    
    print("\n📋 하드코딩 Agent (기존 agent_framework.py):")
    print("   ✅ 장점:")
    print("     - 예측 가능한 동작")
    print("     - 빠른 실행 속도")
    print("     - 디버깅 용이")
    print("   ❌ 단점:")
    print("     - 제한적인 상황 대응")
    print("     - 새로운 시나리오에 취약")
    print("     - if-else 로직에 의존")
    
    print("\n🧠 LLM Agent (llm_agent.py):")
    print("   ✅ 장점:")
    print("     - 실제 추론 능력")
    print("     - 창의적 문제 해결")
    print("     - 자연스러운 사고 과정")
    print("   ❌ 단점:")
    print("     - API 키 필요")
    print("     - 비용 발생")
    print("     - 예측 불가능성")
    
    print("\n🎭 Simple Agent (simple_agent.py):")
    print("   ✅ 장점:")
    print("     - 외부 의존성 없음")
    print("     - 실제 추론 과정 시뮬레이션")
    print("     - 학습 목적에 최적화")
    print("   ❌ 단점:")
    print("     - 제한적인 지능")
    print("     - 패턴 기반 동작")
    print("     - 실제 LLM 대비 성능 제한")
    
    print("\n🎯 사용 권장 시나리오:")
    print("   📚 학습 단계: Simple Agent")
    print("   🧪 프로토타입: Simple Agent → LLM Agent")
    print("   🚀 프로덕션: LLM Agent")


def main():
    """메인 실행 함수"""
    print("=== 간단한 시뮬레이션 Agent 예제 ===")
    print("🎭 외부 라이브러리 없이 순수 Python으로 구현한 Agent입니다.")
    print("🧠 실제 LLM의 추론 과정을 시뮬레이션하여 보여줍니다.\n")
    
    # Agent 유형 비교
    compare_agent_types()
    
    # 시나리오 테스트
    demonstrate_agent_scenarios()
    
    # 대화형 데모 선택
    print(f"\n{'='*80}")
    choice = input("대화형 Simple Agent를 체험해보시겠습니까? (y/n): ").strip().lower()
    
    if choice in ['y', 'yes', '예', 'ㅇ']:
        interactive_simple_agent()
    
    print(f"\n🎉 Simple Agent 예제 완료!")
    
    print(f"\n💡 핵심 포인트:")
    print("1. 🎭 시뮬레이션으로도 Agent의 추론 과정을 이해할 수 있습니다")
    print("2. 🧠 ReAct 패턴 (Think → Act → Observe)의 실제 구현")
    print("3. 🔧 MCP 도구들과의 완벽한 통합")
    print("4. 📊 실행 과정 추적 및 결과 분석")
    
    print(f"\n🚀 다음 단계:")
    print("   - 실제 LLM 연동 (API 키 있을 때)")
    print("   - 더 복잡한 추론 로직 구현")
    print("   - 멀티 Agent 시스템 구축")
    
    print(f"\n🎯 이제 Agent의 핵심 동작 원리를 완전히 이해했습니다!")


if __name__ == "__main__":
    main()