"""
AI Agent 기본 프레임워크

RAG 시스템과 MCP 서버를 통합하여 자율적으로 작업을 수행하는 AI Agent를 구현합니다.
"""

import json
import logging
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum
import time

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AgentState(Enum):
    """Agent 상태"""
    IDLE = "idle"
    THINKING = "thinking"
    ACTING = "acting"
    OBSERVING = "observing"
    COMPLETED = "completed"
    ERROR = "error"


@dataclass
class AgentStep:
    """Agent 실행 단계"""
    step_number: int
    step_type: str  # "thought", "action", "observation"
    content: str
    timestamp: float
    success: bool = True
    error: Optional[str] = None


@dataclass
class AgentTask:
    """Agent 작업 정의"""
    task_id: str
    description: str
    goal: str
    context: Dict[str, Any] = None
    max_steps: int = 10
    timeout: int = 300  # 5분


class AIAgent:
    """
    AI Agent 기본 클래스
    
    ReAct 패턴 (Reasoning + Acting)을 구현하여
    RAG 시스템으로 정보를 수집하고 MCP 서버로 행동을 실행합니다.
    """
    
    def __init__(self, name: str, rag_system=None, mcp_server=None):
        self.name = name
        self.rag_system = rag_system
        self.mcp_server = mcp_server
        
        self.state = AgentState.IDLE
        self.current_task: Optional[AgentTask] = None
        self.execution_history: List[AgentStep] = []
        self.available_tools: List[Dict] = []
        
        # MCP 도구 목록 로드
        if self.mcp_server:
            self._load_available_tools()
        
        logger.info(f"AI Agent '{name}' 초기화 완료")
    
    def _load_available_tools(self):
        """MCP 서버에서 사용 가능한 도구 목록 로드"""
        try:
            request = '{"action": "list_tools"}'
            response = self.mcp_server.handle_request(request)
            response_data = json.loads(response)
            
            if response_data["success"]:
                self.available_tools = response_data["tools"]
                logger.info(f"✅ {len(self.available_tools)}개 도구 로드 완료")
            else:
                logger.error(f"도구 로드 실패: {response_data.get('error')}")
                
        except Exception as e:
            logger.error(f"도구 로드 중 오류: {str(e)}")
    
    def execute_task(self, task: AgentTask) -> Dict[str, Any]:
        """
        작업 실행 (ReAct 패턴)
        
        1. Think: 상황 분석 및 계획
        2. Act: 도구 실행
        3. Observe: 결과 관찰
        4. 목표 달성까지 반복
        """
        self.current_task = task
        self.state = AgentState.THINKING
        self.execution_history = []
        
        logger.info(f"🚀 작업 시작: {task.description}")
        
        start_time = time.time()
        step_number = 1
        
        try:
            while step_number <= task.max_steps:
                # 시간 초과 체크
                if time.time() - start_time > task.timeout:
                    self._add_step(step_number, "error", "작업 시간 초과", False, "시간 초과")
                    self.state = AgentState.ERROR
                    break
                
                # 1. Think: 현재 상황 분석
                thought = self._think(step_number)
                self._add_step(step_number, "thought", thought)
                
                # 목표 달성 확인
                if self._is_goal_achieved():
                    self.state = AgentState.COMPLETED
                    break
                
                # 2. Act: 행동 결정 및 실행
                self.state = AgentState.ACTING
                action_result = self._act(step_number)
                
                if action_result["success"]:
                    self._add_step(step_number, "action", action_result["description"])
                else:
                    self._add_step(step_number, "action", action_result["description"], 
                                 False, action_result.get("error"))
                
                # 3. Observe: 결과 관찰
                self.state = AgentState.OBSERVING
                observation = self._observe(action_result)
                self._add_step(step_number, "observation", observation)
                
                step_number += 1
            
            # 최종 결과 정리
            if self.state != AgentState.COMPLETED and self.state != AgentState.ERROR:
                self.state = AgentState.ERROR
                self._add_step(step_number, "error", "최대 단계 수 초과", False, "단계 수 초과")
            
            execution_time = time.time() - start_time
            
            return {
                "task_id": task.task_id,
                "success": self.state == AgentState.COMPLETED,
                "final_state": self.state.value,
                "execution_time": execution_time,
                "total_steps": len(self.execution_history),
                "steps": [
                    {
                        "step": step.step_number,
                        "type": step.step_type,
                        "content": step.content,
                        "success": step.success,
                        "error": step.error
                    }
                    for step in self.execution_history
                ]
            }
            
        except Exception as e:
            logger.error(f"작업 실행 중 오류: {str(e)}")
            self.state = AgentState.ERROR
            return {
                "task_id": task.task_id,
                "success": False,
                "error": str(e),
                "execution_time": time.time() - start_time,
                "steps": []
            }
        
        finally:
            self.state = AgentState.IDLE
            self.current_task = None
    
    def _think(self, step_number: int) -> str:
        """
        현재 상황 분석 및 다음 행동 계획
        
        RAG 시스템을 사용하여 관련 정보를 검색하고
        현재 상황을 분석합니다.
        """
        try:
            # 현재 작업 상황 분석
            context = f"""
현재 작업: {self.current_task.description}
목표: {self.current_task.goal}
단계: {step_number}/{self.current_task.max_steps}

지금까지의 실행 기록:
"""
            
            # 이전 단계들 요약
            for step in self.execution_history[-3:]:  # 최근 3단계만
                context += f"- {step.step_type}: {step.content}\n"
            
            # RAG 시스템으로 관련 정보 검색 (있는 경우)
            if self.rag_system:
                try:
                    rag_result = self.rag_system.query(self.current_task.description)
                    if rag_result["answer"]:
                        context += f"\n관련 정보: {rag_result['answer'][:200]}..."
                except Exception as e:
                    logger.warning(f"RAG 검색 실패: {str(e)}")
            
            # 사용 가능한 도구 목록
            tools_info = "사용 가능한 도구들:\n"
            for tool in self.available_tools[:5]:  # 상위 5개만
                tools_info += f"- {tool['name']}: {tool['description']}\n"
            
            # 간단한 추론 로직 (실제로는 LLM이 담당)
            if step_number == 1:
                thought = f"작업을 시작합니다. 목표 달성을 위해 필요한 정보를 수집하고 적절한 도구를 선택해야 합니다."
            elif len(self.execution_history) > 0:
                last_step = self.execution_history[-1]
                if last_step.success:
                    thought = f"이전 단계가 성공했습니다. 다음 단계로 진행하겠습니다."
                else:
                    thought = f"이전 단계에서 오류가 발생했습니다: {last_step.error}. 다른 방법을 시도하겠습니다."
            else:
                thought = f"현재 상황을 분석하고 다음 행동을 계획하겠습니다."
            
            return thought
            
        except Exception as e:
            logger.error(f"사고 과정 중 오류: {str(e)}")
            return f"사고 과정에서 오류가 발생했습니다: {str(e)}"
    
    def _act(self, step_number: int) -> Dict[str, Any]:
        """
        행동 실행 (MCP 도구 사용)
        """
        try:
            # 간단한 행동 결정 로직 (실제로는 LLM이 담당)
            if not self.available_tools:
                return {
                    "success": False,
                    "description": "사용 가능한 도구가 없습니다",
                    "error": "도구 없음"
                }
            
            # 작업 유형에 따른 도구 선택
            selected_tool = None
            parameters = {}
            
            # 파일 관련 작업
            if "파일" in self.current_task.description or "문서" in self.current_task.description:
                for tool in self.available_tools:
                    if "file" in tool["name"] or "list" in tool["name"]:
                        selected_tool = tool
                        if "list" in tool["name"]:
                            parameters = {"directory": "."}
                        break
            
            # 정보 검색 작업
            elif "날씨" in self.current_task.description:
                for tool in self.available_tools:
                    if "weather" in tool["name"]:
                        selected_tool = tool
                        parameters = {"city": "서울"}
                        break
            
            # 뉴스 검색 작업
            elif "뉴스" in self.current_task.description:
                for tool in self.available_tools:
                    if "news" in tool["name"]:
                        selected_tool = tool
                        parameters = {"country": "kr", "max_articles": 3}
                        break
            
            # 기본 도구 선택
            if not selected_tool:
                selected_tool = self.available_tools[0]
                parameters = {}
            
            # 도구 실행
            request_data = {
                "action": "execute_tool",
                "tool_name": selected_tool["name"],
                "parameters": parameters,
                "request_id": f"agent_step_{step_number}"
            }
            
            request_json = json.dumps(request_data)
            response_json = self.mcp_server.handle_request(request_json)
            response = json.loads(response_json)
            
            if response["success"]:
                return {
                    "success": True,
                    "description": f"{selected_tool['name']} 도구를 실행했습니다",
                    "tool_name": selected_tool["name"],
                    "parameters": parameters,
                    "result": response["result"]
                }
            else:
                return {
                    "success": False,
                    "description": f"{selected_tool['name']} 도구 실행 실패",
                    "error": response.get("error", "알 수 없는 오류")
                }
                
        except Exception as e:
            logger.error(f"행동 실행 중 오류: {str(e)}")
            return {
                "success": False,
                "description": "행동 실행 중 오류 발생",
                "error": str(e)
            }
    
    def _observe(self, action_result: Dict[str, Any]) -> str:
        """
        행동 결과 관찰 및 분석
        """
        try:
            if action_result["success"]:
                result = action_result.get("result", {})
                
                # 결과 유형에 따른 관찰
                if isinstance(result, dict):
                    if "summary" in result:
                        observation = f"작업이 성공했습니다. {result['summary']}"
                    elif "total_files" in result:
                        observation = f"파일 목록을 조회했습니다. 총 {result['total_files']}개 파일이 있습니다."
                    elif "temperature" in result:
                        observation = f"날씨 정보를 가져왔습니다. {result.get('summary', '날씨 정보 조회 완료')}"
                    else:
                        observation = f"작업이 성공적으로 완료되었습니다."
                else:
                    observation = f"작업 결과: {str(result)[:100]}..."
                
                return observation
            else:
                return f"작업이 실패했습니다: {action_result.get('error', '알 수 없는 오류')}"
                
        except Exception as e:
            logger.error(f"관찰 과정 중 오류: {str(e)}")
            return f"관찰 과정에서 오류가 발생했습니다: {str(e)}"
    
    def _is_goal_achieved(self) -> bool:
        """
        목표 달성 여부 확인
        
        간단한 휴리스틱으로 판단 (실제로는 더 정교한 로직 필요)
        """
        try:
            # 최소 1개 이상의 성공적인 행동이 있어야 함
            successful_actions = [
                step for step in self.execution_history 
                if step.step_type == "action" and step.success
            ]
            
            # 간단한 목표 달성 조건
            if len(successful_actions) >= 1:
                # 특정 키워드 기반 판단
                if "조회" in self.current_task.goal or "확인" in self.current_task.goal:
                    return True
                elif "생성" in self.current_task.goal or "작성" in self.current_task.goal:
                    return len(successful_actions) >= 1
            
            return False
            
        except Exception as e:
            logger.error(f"목표 달성 확인 중 오류: {str(e)}")
            return False
    
    def _add_step(self, step_number: int, step_type: str, content: str, 
                  success: bool = True, error: Optional[str] = None):
        """실행 단계 기록"""
        step = AgentStep(
            step_number=step_number,
            step_type=step_type,
            content=content,
            timestamp=time.time(),
            success=success,
            error=error
        )
        self.execution_history.append(step)
        
        # 로그 출력
        status = "✅" if success else "❌"
        logger.info(f"{status} Step {step_number} ({step_type}): {content}")
        if error:
            logger.error(f"   오류: {error}")
    
    def get_status(self) -> Dict[str, Any]:
        """현재 Agent 상태 반환"""
        return {
            "name": self.name,
            "state": self.state.value,
            "current_task": self.current_task.description if self.current_task else None,
            "available_tools": len(self.available_tools),
            "execution_steps": len(self.execution_history)
        }


if __name__ == "__main__":
    # 기본 테스트
    agent = AIAgent("테스트 Agent")
    print(f"Agent 생성 완료: {agent.name}")
    print(f"상태: {agent.get_status()}")