"""
웹 API MCP 서버 예제

실제 Gmail MCP, Slack MCP, Notion MCP 등이 하는 일을 시뮬레이션합니다.
LLM → MCP Server → 여러 외부 API들
"""

import sys
import json
from pathlib import Path

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

from src.mcp.mcp_server import MCPServer, MCPTool
from src.mcp.tools.web_api_tools import WEB_API_TOOLS


class AdvancedMCPClient:
    """
    고급 MCP 클라이언트 - 실제 LLM의 동작을 시뮬레이션
    """
    
    def __init__(self, server: MCPServer):
        self.server = server
        self.available_tools = []
        self.conversation_history = []
        self._load_tools()
    
    def _load_tools(self):
        """서버에서 사용 가능한 도구 목록을 가져옴"""
        request = '{"action": "list_tools"}'
        response = self.server.handle_request(request)
        response_data = json.loads(response)
        
        if response_data["success"]:
            self.available_tools = response_data["tools"]
            print(f"✅ {len(self.available_tools)}개의 도구를 로드했습니다.")
        else:
            print(f"❌ 도구 로드 실패: {response_data.get('error')}")
    
    def call_tool(self, tool_name: str, parameters: dict = None) -> dict:
        """도구 호출"""
        if parameters is None:
            parameters = {}
        
        request_data = {
            "action": "execute_tool",
            "tool_name": tool_name,
            "parameters": parameters,
            "request_id": f"advanced_client_{len(self.conversation_history)}"
        }
        
        request_json = json.dumps(request_data)
        response_json = self.server.handle_request(request_json)
        response = json.loads(response_json)
        
        # 대화 히스토리에 추가
        self.conversation_history.append({
            "request": request_data,
            "response": response
        })
        
        return response
    
    def simulate_complex_workflow(self):
        """복잡한 워크플로우 시뮬레이션"""
        print("\n🤖 LLM 시뮬레이션: 복합 작업 수행")
        print("시나리오: 날씨 확인 → 뉴스 조회 → 팀에 알림")
        
        # 1단계: 날씨 확인
        print("\n1️⃣ LLM: '서울 날씨 어때?'")
        weather_response = self.call_tool("get_weather", {
            "city": "서울",
            "country": "KR"
        })
        
        if weather_response["success"]:
            weather_data = weather_response["result"]
            print(f"   🌤️  {weather_data['summary']}")
            current_weather = weather_data['summary']
        else:
            print(f"   ❌ 날씨 조회 실패: {weather_response['error']}")
            current_weather = "날씨 정보 없음"
        
        # 2단계: 관련 뉴스 조회
        print("\n2️⃣ LLM: '최신 기술 뉴스도 확인해줘'")
        news_response = self.call_tool("get_news", {
            "country": "kr",
            "category": "technology",
            "max_articles": 3
        })
        
        if news_response["success"]:
            news_data = news_response["result"]
            print(f"   📰 {news_data['summary']}")
            
            # 주요 뉴스 제목들
            top_headlines = []
            for article in news_data['articles']:
                top_headlines.append(article['title'])
                print(f"     - {article['title']}")
        else:
            print(f"   ❌ 뉴스 조회 실패: {news_response['error']}")
            top_headlines = ["뉴스 정보 없음"]
        
        # 3단계: 팀에 종합 리포트 전송
        print("\n3️⃣ LLM: '팀 채널에 오늘의 브리핑 보내줘'")
        
        # 종합 메시지 작성
        briefing_message = f"""📅 오늘의 브리핑

🌤️ 날씨 정보:
{current_weather}

📰 주요 기술 뉴스:
"""
        for i, headline in enumerate(top_headlines, 1):
            briefing_message += f"{i}. {headline}\n"
        
        briefing_message += "\n좋은 하루 되세요! 🚀"
        
        slack_response = self.call_tool("send_slack_message", {
            "channel": "general",
            "text": briefing_message,
            "username": "Daily Briefing Bot"
        })
        
        if slack_response["success"]:
            slack_data = slack_response["result"]
            print(f"   💬 {slack_data['summary']}")
            print(f"   📝 전송된 메시지 길이: {len(briefing_message)} 문자")
        else:
            print(f"   ❌ 메시지 전송 실패: {slack_response['error']}")
        
        # 4단계: 작업 완료 요약
        print("\n4️⃣ 작업 완료 요약:")
        print(f"   ✅ 총 {len(self.conversation_history)}개의 도구를 사용했습니다")
        print("   📊 수행된 작업:")
        print("     - 날씨 API 호출")
        print("     - 뉴스 API 호출") 
        print("     - Slack API 호출")
        print("     - 데이터 통합 및 메시지 생성")
    
    def demonstrate_error_handling(self):
        """에러 처리 시연"""
        print("\n🚨 에러 처리 시연")
        
        # 잘못된 도구 호출
        print("\n1. 존재하지 않는 도구 호출:")
        response = self.call_tool("nonexistent_tool", {})
        print(f"   결과: {response['error']}")
        
        # 잘못된 파라미터
        print("\n2. 필수 파라미터 누락:")
        response = self.call_tool("send_slack_message", {"text": "메시지"})  # channel 누락
        print(f"   결과: {response['error']}")
        
        print("\n✅ MCP 서버가 에러를 적절히 처리하고 있습니다!")


def main():
    """메인 실행 함수"""
    print("=== 웹 API MCP 서버 예제 ===")
    print("실제 Gmail MCP, Slack MCP 등의 동작을 시뮬레이션합니다.\n")
    
    # 1. MCP 서버 생성
    print("🚀 고급 MCP 서버 초기화 중...")
    server = MCPServer("멀티 API MCP 서버")
    
    # 2. 웹 API 도구들 등록
    print("🔧 웹 API 도구들 등록 중...")
    for tool_config in WEB_API_TOOLS:
        tool = MCPTool(
            name=tool_config["name"],
            description=tool_config["description"],
            parameters=tool_config["parameters"],
            function=tool_config["function"]
        )
        server.register_tool(tool)
    
    print(f"✅ {len(WEB_API_TOOLS)}개 웹 API 도구 등록 완료!")
    
    # 3. 고급 클라이언트 생성
    print("\n🤖 고급 MCP 클라이언트 생성 중...")
    client = AdvancedMCPClient(server)
    
    # 4. 사용 가능한 도구 목록 출력
    print("\n🛠️  등록된 웹 API 도구들:")
    for i, tool in enumerate(client.available_tools, 1):
        print(f"{i}. {tool['name']}: {tool['description']}")
    
    # 5. 복합 워크플로우 시연
    client.simulate_complex_workflow()
    
    # 6. 에러 처리 시연
    client.demonstrate_error_handling()
    
    print("\n🎉 웹 API MCP 예제 완료!")
    
    print("\n💡 핵심 포인트:")
    print("1. MCP 서버 = 여러 API들의 통합 인터페이스")
    print("2. 각 도구 = 복잡한 API 호출들의 추상화")
    print("3. LLM은 간단한 함수 호출만 하면 됨")
    print("4. MCP가 실제 API 호출, 에러 처리, 데이터 변환 담당")
    
    print("\n🔍 실제 MCP 서버들:")
    print("- Gmail MCP: 이메일 전송, 읽기, 검색 등")
    print("- Slack MCP: 메시지 전송, 채널 관리 등") 
    print("- Notion MCP: 페이지 생성, 데이터베이스 쿼리 등")
    print("- GitHub MCP: 리포지토리 관리, 이슈 생성 등")


if __name__ == "__main__":
    main()