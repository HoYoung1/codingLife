"""
간단한 시뮬레이션 AI Agent

외부 라이브러리 의존성 없이 순수 Python으로 구현한 Agent입니다.
실제 LLM의 추론 과정을 시뮬레이션하여 Agent의 동작 원리를 보여줍니다.
"""

import json
import time
import random
from typing import Dict, List, Any, Optional
from dataclasses import dataclass


@dataclass
class AgentStep:
    """Agent 실행 단계"""
    step_number: int
    step_type: str  # "thought", "action", "observation"
    content: str
    timestamp: float
    success: bool = True


class SimpleAgent:
    """
    간단한 시뮬레이션 Agent
    
    실제 LLM 없이도 지능적인 추론 과정을 시뮬레이션합니다.
    ReAct 패턴(Reasoning + Acting)을 구현하여 단계별로 작업을 수행합니다.
    """
    
    def __init__(self, name: str, mcp_server=None):
        self.name = name
        self.mcp_server = mcp_server
        self.available_tools: List[Dict] = []
        self.execution_history: List[AgentStep] = []
        self.knowledge_base = self._build_knowledge_base()
        
        # MCP 도구 목록 로드
        if self.mcp_server:
            self._load_available_tools()
        
        print(f"🤖 Simple Agent '{name}' 초기화 완료")
    
    def _build_knowledge_base(self) -> Dict[str, Any]:
        """Agent의 지식 베이스 구축"""
        return {
            "task_patterns": {
                "파일": ["list_files", "read_file", "write_file", "get_file_info"],
                "날씨": ["get_weather"],
                "뉴스": ["get_news"],
                "슬랙": ["send_slack_message", "get_slack_channels"],
                "정보": ["list_files", "get_weather", "get_news"],
                "리포트": ["list_files", "get_weather", "get_news", "write_file"],
                "분석": ["list_files", "read_file", "get_file_info"],
                "생성": ["write_file", "create_directory"],
                "조회": ["list_files", "get_weather", "get_news", "read_file"]
            },
            "reasoning_templates": {
                "start": [
                    "작업을 시작하겠습니다. 먼저 현재 상황을 파악해야 합니다.",
                    "사용자의 요청을 분석하고 필요한 정보를 수집하겠습니다.",
                    "목표 달성을 위한 단계별 계획을 세우겠습니다."
                ],
                "analyze": [
                    "현재 상황을 분석해보니 {analysis}가 필요합니다.",
                    "수집된 정보를 바탕으로 {next_step}을 진행하겠습니다.",
                    "이전 결과를 검토하고 다음 단계를 계획하겠습니다."
                ],
                "plan": [
                    "{tool_name} 도구를 사용하여 {purpose}을 수행하겠습니다.",
                    "목표 달성을 위해 {action}이 필요하다고 판단됩니다.",
                    "다음 단계로 {next_action}을 실행하겠습니다."
                ],
                "complete": [
                    "작업이 성공적으로 완료되었습니다.",
                    "목표를 달성했습니다. 결과를 정리하겠습니다.",
                    "모든 필요한 작업을 완료했습니다."
                ]
            }
        }
    
    def _load_available_tools(self):
        """MCP 서버에서 사용 가능한 도구 목록 로드"""
        try:
            request = '{"action": "list_tools"}'
            response = self.mcp_server.handle_request(request)
            response_data = json.loads(response)
            
            if response_data["success"]:
                self.available_tools = response_data["tools"]
                print(f"✅ {len(self.available_tools)}개 도구 로드 완료")
            else:
                print(f"❌ 도구 로드 실패: {response_data.get('error')}")
                
        except Exception as e:
            print(f"❌ 도구 로드 중 오류: {str(e)}")
    
    def execute_task(self, task_description: str, max_steps: int = 8) -> Dict[str, Any]:
        """
        작업 실행 (ReAct 패턴)
        
        1. Think: 상황 분석 및 계획
        2. Act: 도구 실행
        3. Observe: 결과 관찰
        4. 목표 달성까지 반복
        """
        print(f"\n🚀 작업 시작: {task_description}")
        
        self.execution_history = []
        start_time = time.time()
        
        try:
            for step in range(1, max_steps + 1):
                print(f"\n📍 Step {step}: 사고 과정")
                
                # 1. Think: 현재 상황 분석 및 계획
                thought = self._simulate_thinking(task_description, step)
                self._add_step(step, "thought", thought)
                
                # 목표 달성 확인
                if self._is_goal_achieved(thought, step):
                    print("🎯 목표 달성 완료!")
                    break
                
                # 2. Act: 도구 선택 및 실행
                print(f"🎬 Step {step}: 행동 실행")
                action_result = self._simulate_action(task_description, thought, step)
                self._add_step(step, "action", json.dumps(action_result, ensure_ascii=False))
                
                # 3. Observe: 결과 관찰 및 분석
                print(f"👁️  Step {step}: 결과 관찰")
                observation = self._simulate_observation(action_result, step)
                self._add_step(step, "observation", observation)
                
                # 약간의 지연 (실제 처리 시뮬레이션)
                time.sleep(0.5)
            
            execution_time = time.time() - start_time
            
            return {
                "success": True,
                "task": task_description,
                "execution_time": execution_time,
                "total_steps": len([s for s in self.execution_history if s.step_type == "thought"]),
                "history": [
                    {
                        "step": s.step_number,
                        "type": s.step_type,
                        "content": s.content,
                        "success": s.success
                    }
                    for s in self.execution_history
                ],
                "final_summary": self._generate_summary(task_description)
            }
            
        except Exception as e:
            print(f"❌ 작업 실행 중 오류: {str(e)}")
            return {
                "success": False,
                "error": str(e),
                "task": task_description,
                "history": []
            }
    
    def _simulate_thinking(self, task: str, step: int) -> str:
        """사고 과정 시뮬레이션"""
        
        # 작업 분석
        task_lower = task.lower()
        relevant_tools = []
        
        # 작업 유형별 도구 매칭
        for keyword, tools in self.knowledge_base["task_patterns"].items():
            if keyword in task_lower:
                relevant_tools.extend(tools)
        
        # 중복 제거
        relevant_tools = list(set(relevant_tools))
        
        # 단계별 사고 과정
        if step == 1:
            # 첫 번째 단계: 작업 분석
            template = random.choice(self.knowledge_base["reasoning_templates"]["start"])
            
            if "파일" in task_lower or "문서" in task_lower:
                analysis = "현재 디렉토리의 파일 상황을 파악"
                next_step = "파일 목록 조회"
            elif "날씨" in task_lower:
                analysis = "날씨 정보 수집"
                next_step = "날씨 API 호출"
            elif "뉴스" in task_lower:
                analysis = "최신 뉴스 정보 수집"
                next_step = "뉴스 API 호출"
            elif "리포트" in task_lower or "보고서" in task_lower:
                analysis = "정보 수집 및 문서 생성"
                next_step = "필요한 정보들을 순차적으로 수집"
            else:
                analysis = "현재 상황 파악"
                next_step = "기본 정보 수집"
            
            thought = f"{template} {analysis}이 필요하고, {next_step}부터 시작하겠습니다."
            
        elif step <= 3:
            # 중간 단계: 분석 및 계획
            template = random.choice(self.knowledge_base["reasoning_templates"]["analyze"])
            
            if relevant_tools:
                tool_name = relevant_tools[0] if len(relevant_tools) > 0 else "적절한 도구"
                thought = template.format(
                    analysis="추가 정보 수집",
                    next_step=f"{tool_name} 도구 사용",
                    tool_name=tool_name,
                    purpose="필요한 정보 획득"
                )
            else:
                thought = "현재까지의 결과를 분석하고 다음 단계를 계획하고 있습니다."
                
        else:
            # 후반 단계: 완료 준비
            if step >= 6 or "완료" in task_lower:
                template = random.choice(self.knowledge_base["reasoning_templates"]["complete"])
                thought = f"{template} 수집된 정보를 정리하여 최종 결과를 제공하겠습니다."
            else:
                template = random.choice(self.knowledge_base["reasoning_templates"]["plan"])
                thought = template.format(
                    tool_name="추가 도구",
                    purpose="작업 완성",
                    action="정보 정리",
                    next_action="결과 생성"
                )
        
        return thought
    
    def _simulate_action(self, task: str, thought: str, step: int) -> Dict[str, Any]:
        """행동 시뮬레이션 (도구 선택 및 실행)"""
        
        # 작업 기반 도구 선택
        task_lower = task.lower()
        selected_tool = None
        parameters = {}
        
        # 도구 선택 로직
        if step == 1:
            # 첫 번째 단계: 상황 파악
            if "파일" in task_lower or "문서" in task_lower or "리포트" in task_lower:
                selected_tool = "list_files"
                parameters = {"directory": "."}
            elif "날씨" in task_lower:
                selected_tool = "get_weather"
                parameters = {"city": "서울", "country": "KR"}
            elif "뉴스" in task_lower:
                selected_tool = "get_news"
                parameters = {"country": "kr", "max_articles": 5}
            else:
                selected_tool = "list_files"
                parameters = {"directory": "."}
                
        elif step == 2:
            # 두 번째 단계: 추가 정보 수집
            if "리포트" in task_lower or "분석" in task_lower:
                if "날씨" in task_lower:
                    selected_tool = "get_weather"
                    parameters = {"city": "서울"}
                elif "뉴스" in task_lower:
                    selected_tool = "get_news"
                    parameters = {"country": "kr", "category": "technology"}
                else:
                    selected_tool = "read_file"
                    parameters = {"file_path": "README.md"}
            elif "파일" in task_lower:
                selected_tool = "get_file_info"
                parameters = {"file_path": "README.md"}
            else:
                selected_tool = "get_weather"
                parameters = {"city": "서울"}
                
        elif step >= 3:
            # 후반 단계: 결과 생성 또는 추가 작업
            if "생성" in task_lower or "작성" in task_lower or "리포트" in task_lower:
                selected_tool = "write_file"
                parameters = {
                    "file_path": f"agent_report_{int(time.time())}.md",
                    "content": self._generate_report_content(task),
                    "overwrite": True
                }
            elif "슬랙" in task_lower or "메시지" in task_lower:
                selected_tool = "send_slack_message"
                parameters = {
                    "channel": "general",
                    "text": f"Agent 작업 완료: {task}"
                }
            else:
                selected_tool = "get_news"
                parameters = {"country": "kr", "max_articles": 3}
        
        # 도구가 선택되지 않은 경우 기본 도구 사용
        if not selected_tool and self.available_tools:
            selected_tool = self.available_tools[0]["name"]
            parameters = {}
        
        # 실제 도구 실행
        if selected_tool and self.mcp_server:
            try:
                request_data = {
                    "action": "execute_tool",
                    "tool_name": selected_tool,
                    "parameters": parameters,
                    "request_id": f"simple_agent_step_{step}"
                }
                
                request_json = json.dumps(request_data)
                response_json = self.mcp_server.handle_request(request_json)
                response = json.loads(response_json)
                
                return {
                    "success": response["success"],
                    "tool_name": selected_tool,
                    "parameters": parameters,
                    "result": response.get("result"),
                    "error": response.get("error")
                }
                
            except Exception as e:
                return {
                    "success": False,
                    "tool_name": selected_tool,
                    "parameters": parameters,
                    "error": str(e)
                }
        else:
            # MCP 서버가 없는 경우 시뮬레이션
            return {
                "success": True,
                "tool_name": selected_tool or "simulation_tool",
                "parameters": parameters,
                "result": f"시뮬레이션 결과: {selected_tool} 도구를 성공적으로 실행했습니다."
            }
    
    def _simulate_observation(self, action_result: Dict[str, Any], step: int) -> str:
        """결과 관찰 시뮬레이션"""
        
        if action_result["success"]:
            tool_name = action_result["tool_name"]
            result = action_result.get("result", {})
            
            # 도구별 관찰 내용 생성
            if tool_name == "list_files":
                if isinstance(result, dict) and "total_files" in result:
                    observation = f"파일 목록을 성공적으로 조회했습니다. 총 {result['total_files']}개의 파일이 있습니다. 이제 필요한 파일들을 분석할 수 있습니다."
                else:
                    observation = "파일 목록 조회가 완료되었습니다. 디렉토리 구조를 파악했습니다."
                    
            elif tool_name == "get_weather":
                if isinstance(result, dict) and "summary" in result:
                    observation = f"날씨 정보를 성공적으로 가져왔습니다. {result['summary']} 이 정보를 활용하여 다음 단계를 진행하겠습니다."
                else:
                    observation = "날씨 정보 조회가 완료되었습니다. 현재 기상 상황을 파악했습니다."
                    
            elif tool_name == "get_news":
                if isinstance(result, dict) and "total_articles" in result:
                    observation = f"뉴스 정보를 성공적으로 수집했습니다. {result['total_articles']}개의 기사를 확인했습니다. 주요 동향을 파악할 수 있었습니다."
                else:
                    observation = "최신 뉴스 정보를 성공적으로 수집했습니다. 현재 이슈들을 파악했습니다."
                    
            elif tool_name == "write_file":
                observation = "파일 생성이 성공적으로 완료되었습니다. 수집된 정보를 체계적으로 정리하여 문서화했습니다."
                
            elif tool_name == "send_slack_message":
                observation = "Slack 메시지 전송이 완료되었습니다. 팀에게 작업 결과를 성공적으로 공유했습니다."
                
            else:
                observation = f"{tool_name} 도구 실행이 성공적으로 완료되었습니다. 예상한 결과를 얻었습니다."
            
            # 단계별 추가 분석
            if step >= 3:
                observation += " 충분한 정보를 수집했으므로 작업을 마무리할 준비가 되었습니다."
                
        else:
            error = action_result.get("error", "알 수 없는 오류")
            observation = f"도구 실행 중 문제가 발생했습니다: {error}. 다른 방법을 시도해보겠습니다."
        
        return observation
    
    def _is_goal_achieved(self, thought: str, step: int) -> bool:
        """목표 달성 여부 확인"""
        
        # 완료 키워드 확인
        completion_keywords = ["완료", "달성", "성공", "끝", "마무리", "완성"]
        thought_lower = thought.lower()
        
        # 키워드 기반 판단
        if any(keyword in thought_lower for keyword in completion_keywords):
            return True
        
        # 단계 수 기반 판단 (너무 많은 단계 방지)
        if step >= 6:
            return True
        
        # 성공적인 액션이 충분히 수행된 경우
        successful_actions = len([s for s in self.execution_history if s.step_type == "action" and s.success])
        if successful_actions >= 3:
            return True
        
        return False
    
    def _generate_report_content(self, task: str) -> str:
        """리포트 내용 생성"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        
        content = f"""# Agent 작업 리포트

## 작업 정보
- 요청: {task}
- 실행 시간: {timestamp}
- Agent: {self.name}

## 실행 결과
작업이 성공적으로 완료되었습니다.

### 수행된 작업들
"""
        
        # 실행 기록 추가
        actions = [s for s in self.execution_history if s.step_type == "action"]
        for i, action in enumerate(actions, 1):
            try:
                action_data = json.loads(action.content)
                tool_name = action_data.get("tool_name", "unknown")
                content += f"{i}. {tool_name} 도구 실행\n"
            except:
                content += f"{i}. 작업 수행\n"
        
        content += f"""
## 결론
요청하신 작업을 단계별로 분석하고 실행하여 성공적으로 완료했습니다.
총 {len(actions)}개의 도구를 사용하여 목표를 달성했습니다.

---
Generated by {self.name}
"""
        
        return content
    
    def _generate_summary(self, task: str) -> str:
        """최종 요약 생성"""
        actions = [s for s in self.execution_history if s.step_type == "action"]
        successful_actions = [s for s in actions if s.success]
        
        summary = f"'{task}' 작업을 성공적으로 완료했습니다. "
        summary += f"총 {len(actions)}개의 도구를 사용했으며, "
        summary += f"그 중 {len(successful_actions)}개가 성공적으로 실행되었습니다. "
        
        # 마지막 관찰 내용 추가
        observations = [s for s in self.execution_history if s.step_type == "observation"]
        if observations:
            last_observation = observations[-1].content
            summary += f"최종 결과: {last_observation[:100]}..."
        
        return summary
    
    def _add_step(self, step_number: int, step_type: str, content: str, success: bool = True):
        """실행 단계 기록"""
        step = AgentStep(
            step_number=step_number,
            step_type=step_type,
            content=content,
            timestamp=time.time(),
            success=success
        )
        self.execution_history.append(step)
        
        # 로그 출력
        status = "✅" if success else "❌"
        print(f"{status} {step_type.title()}: {content[:100]}...")


if __name__ == "__main__":
    # 기본 테스트
    agent = SimpleAgent("테스트 Simple Agent")
    print(f"Agent 생성 완료: {agent.name}")
    
    # 간단한 작업 테스트
    result = agent.execute_task("현재 상황을 파악해주세요", max_steps=3)
    print(f"\n결과: {result['success']}")
    print(f"요약: {result.get('final_summary', 'N/A')}")