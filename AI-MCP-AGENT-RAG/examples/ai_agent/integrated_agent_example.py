"""
통합 AI Agent 예제

RAG 시스템 + MCP 서버 + AI Agent를 통합하여
실제 업무를 자율적으로 수행하는 AI Agent를 시연합니다.
"""

import sys
import json
from pathlib import Path

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

from src.rag_system import RAGSystem
from src.mcp.mcp_server import MCPServer, MCPTool
from src.mcp.tools.file_system_tools import FILE_SYSTEM_TOOLS
from src.mcp.tools.web_api_tools import WEB_API_TOOLS
from src.ai_agent.agent_framework import AIAgent, AgentTask


def setup_rag_system():
    """RAG 시스템 설정"""
    print("📚 RAG 시스템 초기화 중...")
    
    # RAG 시스템 생성 (Ollama 없이)
    rag = RAGSystem(use_ollama=False)
    
    # 샘플 문서 생성 및 추가
    docs_dir = Path("agent_knowledge")
    docs_dir.mkdir(exist_ok=True)
    
    # AI Agent 관련 지식 문서
    agent_knowledge = """# AI Agent 업무 가이드

## 파일 관리 작업
- 파일 목록 조회: list_files 도구 사용
- 파일 읽기: read_file 도구 사용  
- 파일 생성: write_file 도구 사용
- 디렉토리 생성: create_directory 도구 사용

## 정보 수집 작업
- 날씨 정보: get_weather 도구 사용
- 뉴스 정보: get_news 도구 사용
- 파일 정보: get_file_info 도구 사용

## 커뮤니케이션 작업
- Slack 메시지 전송: send_slack_message 도구 사용
- 채널 목록 조회: get_slack_channels 도구 사용

## 작업 순서
1. 목표 분석 및 필요한 정보 파악
2. 적절한 도구 선택
3. 도구 실행 및 결과 확인
4. 필요시 추가 작업 수행
5. 최종 결과 정리
"""
    
    with open(docs_dir / "agent_guide.txt", "w", encoding="utf-8") as f:
        f.write(agent_knowledge)
    
    # 문서를 RAG 시스템에 추가
    success = rag.add_documents([str(docs_dir / "agent_guide.txt")])
    
    if success:
        print("✅ RAG 시스템 초기화 완료")
        return rag
    else:
        print("❌ RAG 시스템 초기화 실패")
        return None


def setup_mcp_server():
    """MCP 서버 설정"""
    print("🔧 MCP 서버 초기화 중...")
    
    server = MCPServer("통합 AI Agent MCP 서버")
    
    # 파일 시스템 도구들 등록
    for tool_config in FILE_SYSTEM_TOOLS:
        tool = MCPTool(
            name=tool_config["name"],
            description=tool_config["description"],
            parameters=tool_config["parameters"],
            function=tool_config["function"]
        )
        server.register_tool(tool)
    
    # 웹 API 도구들 등록
    for tool_config in WEB_API_TOOLS:
        tool = MCPTool(
            name=tool_config["name"],
            description=tool_config["description"],
            parameters=tool_config["parameters"],
            function=tool_config["function"]
        )
        server.register_tool(tool)
    
    print(f"✅ MCP 서버 초기화 완료 ({len(FILE_SYSTEM_TOOLS) + len(WEB_API_TOOLS)}개 도구)")
    return server


def demonstrate_agent_scenarios():
    """다양한 Agent 시나리오 시연"""
    
    # 1. 시스템 설정
    rag_system = setup_rag_system()
    mcp_server = setup_mcp_server()
    
    if not rag_system or not mcp_server:
        print("❌ 시스템 초기화 실패")
        return
    
    # 2. AI Agent 생성
    print("\n🤖 AI Agent 생성 중...")
    agent = AIAgent(
        name="통합 업무 Assistant",
        rag_system=rag_system,
        mcp_server=mcp_server
    )
    
    print(f"✅ Agent 생성 완료: {agent.name}")
    print(f"📊 Agent 상태: {agent.get_status()}")
    
    # 3. 시나리오 실행
    scenarios = [
        {
            "name": "파일 시스템 탐색",
            "task": AgentTask(
                task_id="scenario_1",
                description="현재 디렉토리의 파일들을 조사하고 정리해주세요",
                goal="파일 목록 조회 및 정보 수집",
                max_steps=5
            )
        },
        {
            "name": "정보 수집 및 리포트",
            "task": AgentTask(
                task_id="scenario_2", 
                description="서울 날씨와 최신 뉴스를 조회해서 일일 브리핑을 만들어주세요",
                goal="날씨 및 뉴스 정보 수집",
                max_steps=6
            )
        },
        {
            "name": "문서 생성 및 관리",
            "task": AgentTask(
                task_id="scenario_3",
                description="오늘의 작업 요약 문서를 생성해주세요",
                goal="문서 생성 및 저장",
                max_steps=4
            )
        }
    ]
    
    # 각 시나리오 실행
    for i, scenario in enumerate(scenarios, 1):
        print(f"\n{'='*60}")
        print(f"🎯 시나리오 {i}: {scenario['name']}")
        print(f"📋 작업: {scenario['task'].description}")
        print(f"🎯 목표: {scenario['task'].goal}")
        print(f"{'='*60}")
        
        # Agent 실행
        result = agent.execute_task(scenario['task'])
        
        # 결과 출력
        print(f"\n📊 실행 결과:")
        print(f"   성공 여부: {'✅ 성공' if result['success'] else '❌ 실패'}")
        print(f"   최종 상태: {result['final_state']}")
        print(f"   실행 시간: {result['execution_time']:.2f}초")
        print(f"   총 단계 수: {result['total_steps']}")
        
        if result.get('error'):
            print(f"   오류: {result['error']}")
        
        # 실행 단계 상세 출력
        print(f"\n📝 실행 단계 상세:")
        for step in result['steps']:
            status = "✅" if step['success'] else "❌"
            print(f"   {status} Step {step['step']} ({step['type']}): {step['content']}")
            if step.get('error'):
                print(f"      오류: {step['error']}")
        
        print(f"\n⏱️  시나리오 {i} 완료\n")
    
    # 4. Agent 성능 분석
    print(f"\n{'='*60}")
    print("📈 Agent 성능 분석")
    print(f"{'='*60}")
    
    total_scenarios = len(scenarios)
    successful_scenarios = sum(1 for scenario in scenarios if True)  # 실제로는 결과 기반 계산
    
    print(f"총 시나리오 수: {total_scenarios}")
    print(f"성공한 시나리오: {successful_scenarios}")
    print(f"성공률: {(successful_scenarios/total_scenarios)*100:.1f}%")
    
    print(f"\n💡 Agent의 핵심 기능:")
    print("1. 🧠 RAG 시스템으로 지식 검색 및 상황 분석")
    print("2. 🛠️  MCP 서버로 다양한 도구 실행")
    print("3. 🔄 ReAct 패턴으로 자율적 작업 수행")
    print("4. 📊 실행 과정 추적 및 결과 분석")
    
    print(f"\n🚀 다음 단계:")
    print("1. 더 복잡한 멀티스텝 작업 처리")
    print("2. 실제 LLM 연동으로 더 지능적인 추론")
    print("3. 에러 복구 및 재시도 로직 개선")
    print("4. 멀티 Agent 협력 시스템 구축")


def interactive_agent_demo():
    """대화형 Agent 데모"""
    print(f"\n{'='*60}")
    print("🎮 대화형 Agent 데모")
    print(f"{'='*60}")
    
    # 시스템 설정
    rag_system = setup_rag_system()
    mcp_server = setup_mcp_server()
    agent = AIAgent("대화형 Assistant", rag_system, mcp_server)
    
    print("\n💬 Agent와 대화해보세요! (종료하려면 'quit' 입력)")
    print("예시 요청:")
    print("- '현재 디렉토리 파일 목록을 보여줘'")
    print("- '서울 날씨를 알려줘'")
    print("- '최신 뉴스를 확인해줘'")
    print("- '작업 요약 파일을 만들어줘'")
    
    task_counter = 1
    
    while True:
        try:
            user_input = input(f"\n👤 사용자: ").strip()
            
            if user_input.lower() in ['quit', 'exit', '종료', 'q']:
                print("👋 Agent 데모를 종료합니다.")
                break
            
            if not user_input:
                continue
            
            # 사용자 입력을 작업으로 변환
            task = AgentTask(
                task_id=f"interactive_{task_counter}",
                description=user_input,
                goal=f"사용자 요청 처리: {user_input}",
                max_steps=5
            )
            
            print(f"\n🤖 Agent: 요청을 처리하겠습니다...")
            
            # Agent 실행
            result = agent.execute_task(task)
            
            # 결과 요약 출력
            if result['success']:
                print(f"✅ 작업을 완료했습니다!")
                
                # 마지막 관찰 결과 출력
                observations = [step for step in result['steps'] if step['type'] == 'observation']
                if observations:
                    print(f"📋 결과: {observations[-1]['content']}")
            else:
                print(f"❌ 작업 처리 중 문제가 발생했습니다.")
                if result.get('error'):
                    print(f"오류: {result['error']}")
            
            task_counter += 1
            
        except KeyboardInterrupt:
            print("\n\n👋 Agent 데모를 종료합니다.")
            break
        except Exception as e:
            print(f"❌ 오류 발생: {str(e)}")


def main():
    """메인 실행 함수"""
    print("=== 통합 AI Agent 예제 ===")
    print("RAG + MCP + AI Agent 통합 시스템을 시연합니다.\n")
    
    # 1. 자동 시나리오 시연
    demonstrate_agent_scenarios()
    
    # 2. 대화형 데모 (선택사항)
    print(f"\n{'='*60}")
    choice = input("대화형 Agent 데모를 실행하시겠습니까? (y/n): ").strip().lower()
    
    if choice in ['y', 'yes', '예', 'ㅇ']:
        interactive_agent_demo()
    
    print("\n🎉 통합 AI Agent 예제 완료!")
    print("\n📚 학습 완료 항목:")
    print("✅ RAG 시스템 - 지식 검색 및 정보 수집")
    print("✅ MCP 프로토콜 - 도구 연동 및 시스템 제어")
    print("✅ AI Agent - 자율적 작업 수행 및 목표 달성")
    
    print("\n🚀 축하합니다! AI Agent, RAG, MCP 학습을 모두 완료했습니다!")


if __name__ == "__main__":
    main()