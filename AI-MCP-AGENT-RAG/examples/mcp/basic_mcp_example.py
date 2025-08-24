"""
기본 MCP 서버/클라이언트 예제

LLM → MCP Server → System API 흐름을 보여주는 예제입니다.
"""

import sys
import json
from pathlib import Path

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

from src.mcp.mcp_server import MCPServer, MCPTool
from src.mcp.tools.file_system_tools import FILE_SYSTEM_TOOLS


class SimpleMCPClient:
    """
    간단한 MCP 클라이언트
    
    실제로는 LLM이 이 역할을 하지만, 
    테스트를 위해 간단한 클라이언트를 만들었습니다.
    """
    
    def __init__(self, server: MCPServer):
        self.server = server
        self.available_tools = []
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
    
    def list_available_tools(self):
        """사용 가능한 도구 목록 출력"""
        print("\n🛠️  사용 가능한 도구들:")
        for i, tool in enumerate(self.available_tools, 1):
            print(f"{i}. {tool['name']}: {tool['description']}")
    
    def call_tool(self, tool_name: str, parameters: dict = None) -> dict:
        """도구 호출"""
        if parameters is None:
            parameters = {}
        
        request_data = {
            "action": "execute_tool",
            "tool_name": tool_name,
            "parameters": parameters,
            "request_id": f"client_request_{tool_name}"
        }
        
        request_json = json.dumps(request_data)
        response_json = self.server.handle_request(request_json)
        
        return json.loads(response_json)
    
    def simulate_llm_conversation(self):
        """LLM과의 대화를 시뮬레이션"""
        print("\n🤖 LLM 시뮬레이션: 파일 시스템 작업 수행")
        
        # 시나리오: LLM이 파일 시스템을 탐색하고 파일을 생성하는 상황
        
        print("\n1️⃣ LLM: '현재 디렉토리에 어떤 파일들이 있는지 확인해줘'")
        response = self.call_tool("list_files", {"directory": "."})
        if response["success"]:
            result = response["result"]
            print(f"   📁 디렉토리: {result['directory']}")
            print(f"   📄 파일 수: {result['total_files']}")
            print(f"   📂 폴더 수: {result['total_directories']}")
            
            # 몇 개 파일 이름 출력
            if result['files']:
                print("   주요 파일들:")
                for file in result['files'][:3]:
                    print(f"     - {file['name']}")
        else:
            print(f"   ❌ 오류: {response['error']}")
        
        print("\n2️⃣ LLM: 'MCP 학습 노트를 작성해줘'")
        note_content = """# MCP 학습 노트

## 오늘 배운 내용
- MCP는 LLM과 시스템 API를 연결하는 프로토콜
- LLM → MCP Server → System API 구조
- 도구 등록, 파라미터 검증, 실행 결과 반환

## 구현한 기능
- 기본 MCP 서버
- 파일 시스템 도구들
- 클라이언트 시뮬레이션

## 다음 단계
- 웹 API 도구 구현
- RAG 시스템과 통합
- 실제 LLM 연동
"""
        
        response = self.call_tool("write_file", {
            "file_path": "mcp_learning_notes.md",
            "content": note_content,
            "overwrite": True
        })
        
        if response["success"]:
            result = response["result"]
            print(f"   ✅ 파일 생성 완료: {result['file_path']}")
            print(f"   📝 내용 길이: {result['content_length']} 문자")
        else:
            print(f"   ❌ 오류: {response['error']}")
        
        print("\n3️⃣ LLM: '방금 만든 파일을 읽어서 확인해줘'")
        response = self.call_tool("read_file", {"file_path": "mcp_learning_notes.md"})
        
        if response["success"]:
            result = response["result"]
            print(f"   📖 파일 읽기 완료: {result['file_path']}")
            print(f"   📏 파일 크기: {result['size']} bytes")
            print("   📄 내용 미리보기:")
            lines = result['content'].split('\n')
            for line in lines[:5]:
                print(f"     {line}")
            if len(lines) > 5:
                print(f"     ... (총 {len(lines)}줄)")
        else:
            print(f"   ❌ 오류: {response['error']}")
        
        print("\n4️⃣ LLM: '파일 정보를 자세히 알려줘'")
        response = self.call_tool("get_file_info", {"file_path": "mcp_learning_notes.md"})
        
        if response["success"]:
            result = response["result"]
            print(f"   📊 파일 정보:")
            print(f"     이름: {result['name']}")
            print(f"     타입: {result['type']}")
            print(f"     크기: {result['size']} bytes")
            print(f"     확장자: {result.get('extension', 'N/A')}")
        else:
            print(f"   ❌ 오류: {response['error']}")


def main():
    """메인 실행 함수"""
    print("=== MCP 기본 예제 ===")
    print("LLM → MCP Server → System API 흐름을 시연합니다.\n")
    
    # 1. MCP 서버 생성
    print("🚀 MCP 서버 초기화 중...")
    server = MCPServer("파일 시스템 MCP 서버")
    
    # 2. 파일 시스템 도구들 등록
    print("🔧 파일 시스템 도구들 등록 중...")
    for tool_config in FILE_SYSTEM_TOOLS:
        tool = MCPTool(
            name=tool_config["name"],
            description=tool_config["description"],
            parameters=tool_config["parameters"],
            function=tool_config["function"]
        )
        server.register_tool(tool)
    
    print(f"✅ {len(FILE_SYSTEM_TOOLS)}개 도구 등록 완료!")
    
    # 3. 클라이언트 생성 (LLM 역할)
    print("\n🤖 MCP 클라이언트 생성 중...")
    client = SimpleMCPClient(server)
    
    # 4. 사용 가능한 도구 목록 출력
    client.list_available_tools()
    
    # 5. LLM 대화 시뮬레이션
    client.simulate_llm_conversation()
    
    print("\n🎉 MCP 기본 예제 완료!")
    print("\n💡 이해한 내용:")
    print("1. MCP 서버가 도구들을 관리하고 실행합니다")
    print("2. 클라이언트(LLM)가 JSON으로 요청을 보냅니다")
    print("3. 서버가 실제 시스템 API를 호출합니다")
    print("4. 결과를 다시 JSON으로 반환합니다")
    
    print("\n🔍 생성된 파일을 확인해보세요:")
    print("- mcp_learning_notes.md")


if __name__ == "__main__":
    main()