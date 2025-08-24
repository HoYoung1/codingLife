"""
MCP (Model Context Protocol) 서버 기본 구현

MCP는 LLM이 외부 도구와 상호작용할 수 있게 해주는 프로토콜입니다.
"""

import json
import logging
from typing import Dict, List, Any, Callable, Optional
from dataclasses import dataclass
from abc import ABC, abstractmethod

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class MCPTool:
    """MCP 도구 정의"""
    name: str
    description: str
    parameters: Dict[str, Any]  # JSON Schema 형태
    function: Callable


@dataclass
class MCPRequest:
    """MCP 요청 구조"""
    tool_name: str
    parameters: Dict[str, Any]
    request_id: Optional[str] = None


@dataclass
class MCPResponse:
    """MCP 응답 구조"""
    success: bool
    result: Any = None
    error: Optional[str] = None
    request_id: Optional[str] = None


class MCPServer:
    """
    MCP 서버 구현
    
    LLM → MCP Server → System API 의 중간 역할을 담당
    """
    
    def __init__(self, name: str = "Basic MCP Server"):
        self.name = name
        self.tools: Dict[str, MCPTool] = {}
        logger.info(f"MCP 서버 '{name}' 초기화 완료")
    
    def register_tool(self, tool: MCPTool):
        """도구를 서버에 등록"""
        self.tools[tool.name] = tool
        logger.info(f"도구 등록: {tool.name}")
    
    def get_available_tools(self) -> List[Dict[str, Any]]:
        """사용 가능한 도구 목록 반환 (LLM이 이해할 수 있는 형태)"""
        tools_info = []
        
        for tool_name, tool in self.tools.items():
            tool_info = {
                "name": tool.name,
                "description": tool.description,
                "parameters": tool.parameters
            }
            tools_info.append(tool_info)
        
        return tools_info
    
    def execute_tool(self, request: MCPRequest) -> MCPResponse:
        """도구 실행"""
        try:
            # 도구 존재 확인
            if request.tool_name not in self.tools:
                return MCPResponse(
                    success=False,
                    error=f"도구 '{request.tool_name}'를 찾을 수 없습니다.",
                    request_id=request.request_id
                )
            
            tool = self.tools[request.tool_name]
            
            # 파라미터 검증 (간단한 버전)
            required_params = tool.parameters.get("required", [])
            for param in required_params:
                if param not in request.parameters:
                    return MCPResponse(
                        success=False,
                        error=f"필수 파라미터 '{param}'가 누락되었습니다.",
                        request_id=request.request_id
                    )
            
            # 도구 실행
            logger.info(f"도구 실행: {request.tool_name} with {request.parameters}")
            result = tool.function(**request.parameters)
            
            return MCPResponse(
                success=True,
                result=result,
                request_id=request.request_id
            )
            
        except Exception as e:
            logger.error(f"도구 실행 실패: {str(e)}")
            return MCPResponse(
                success=False,
                error=f"도구 실행 중 오류 발생: {str(e)}",
                request_id=request.request_id
            )
    
    def handle_request(self, request_json: str) -> str:
        """JSON 요청을 처리하고 JSON 응답 반환"""
        try:
            request_data = json.loads(request_json)
            
            # 도구 목록 요청
            if request_data.get("action") == "list_tools":
                tools = self.get_available_tools()
                response = {
                    "success": True,
                    "tools": tools
                }
                return json.dumps(response, ensure_ascii=False, indent=2)
            
            # 도구 실행 요청
            elif request_data.get("action") == "execute_tool":
                request = MCPRequest(
                    tool_name=request_data["tool_name"],
                    parameters=request_data.get("parameters", {}),
                    request_id=request_data.get("request_id")
                )
                
                response = self.execute_tool(request)
                response_dict = {
                    "success": response.success,
                    "result": response.result,
                    "error": response.error,
                    "request_id": response.request_id
                }
                return json.dumps(response_dict, ensure_ascii=False, indent=2)
            
            else:
                error_response = {
                    "success": False,
                    "error": "알 수 없는 액션입니다."
                }
                return json.dumps(error_response, ensure_ascii=False, indent=2)
                
        except json.JSONDecodeError:
            error_response = {
                "success": False,
                "error": "잘못된 JSON 형식입니다."
            }
            return json.dumps(error_response, ensure_ascii=False, indent=2)
        except Exception as e:
            error_response = {
                "success": False,
                "error": f"요청 처리 중 오류 발생: {str(e)}"
            }
            return json.dumps(error_response, ensure_ascii=False, indent=2)


# 기본 도구들 정의
def get_current_time() -> str:
    """현재 시간 반환"""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def calculate(expression: str) -> str:
    """간단한 계산 수행"""
    try:
        # 보안을 위해 제한된 계산만 허용
        allowed_chars = set("0123456789+-*/(). ")
        if not all(c in allowed_chars for c in expression):
            return "오류: 허용되지 않는 문자가 포함되어 있습니다."
        
        result = eval(expression)
        return f"{expression} = {result}"
    except Exception as e:
        return f"계산 오류: {str(e)}"


def echo_message(message: str) -> str:
    """메시지를 그대로 반환 (테스트용)"""
    return f"Echo: {message}"


# 사용 예시
if __name__ == "__main__":
    # MCP 서버 생성
    server = MCPServer("테스트 MCP 서버")
    
    # 기본 도구들 등록
    server.register_tool(MCPTool(
        name="get_current_time",
        description="현재 시간을 반환합니다",
        parameters={
            "type": "object",
            "properties": {},
            "required": []
        },
        function=get_current_time
    ))
    
    server.register_tool(MCPTool(
        name="calculate",
        description="간단한 수학 계산을 수행합니다",
        parameters={
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "계산할 수식 (예: '2 + 3 * 4')"
                }
            },
            "required": ["expression"]
        },
        function=calculate
    ))
    
    server.register_tool(MCPTool(
        name="echo",
        description="입력받은 메시지를 그대로 반환합니다",
        parameters={
            "type": "object",
            "properties": {
                "message": {
                    "type": "string",
                    "description": "반환할 메시지"
                }
            },
            "required": ["message"]
        },
        function=echo_message
    ))
    
    print("=== MCP 서버 테스트 ===")
    
    # 도구 목록 조회
    print("\n1. 사용 가능한 도구 목록:")
    list_request = '{"action": "list_tools"}'
    response = server.handle_request(list_request)
    print(response)
    
    # 도구 실행 테스트
    print("\n2. 현재 시간 조회:")
    time_request = '{"action": "execute_tool", "tool_name": "get_current_time", "request_id": "test1"}'
    response = server.handle_request(time_request)
    print(response)
    
    print("\n3. 계산 수행:")
    calc_request = '{"action": "execute_tool", "tool_name": "calculate", "parameters": {"expression": "10 + 5 * 2"}, "request_id": "test2"}'
    response = server.handle_request(calc_request)
    print(response)
    
    print("\n4. 에코 테스트:")
    echo_request = '{"action": "execute_tool", "tool_name": "echo", "parameters": {"message": "안녕하세요 MCP!"}, "request_id": "test3"}'
    response = server.handle_request(echo_request)
    print(response)