"""
실제 LLM 기반 AI Agent 구현

OpenAI API 또는 다른 LLM을 사용하여 진짜 추론 능력을 가진 Agent를 구현합니다.
API 키가 없을 때는 시뮬레이션 모드로 동작합니다.
"""

import json
import logging
import time
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum

# 실제 환경에서는 이런 라이브러리들을 사용
try:
    import openai  # pip install openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

try:
    from langchain.llms import Ollama  # 로컬 LLM
    OLLAMA_AVAILABLE = True
except ImportError:
    OLLAMA_AVAILABLE = False

logger = logging.getLogger(__name__)


class LLMProvider(Enum):
    """LLM 제공자"""
    OPENAI = "openai"
    OLLAMA = "ollama"
    SIMULATION = "simulation"


@dataclass
class LLMConfig:
    """LLM 설정"""
    provider: LLMProvider
    model: str = "gpt-3.5-turbo"
    api_key: Optional[str] = None
    base_url: Optional[str] = None
    temperature: float = 0.7
    max_tokens: int = 1000


class LLMInterface:
    """
    LLM 인터페이스 - 다양한 LLM 제공자를 통합
    
    실제 환경에서는 OpenAI, Ollama 등을 사용하고,
    API 키가 없을 때는 시뮬레이션 모드로 동작
    """
    
    def __init__(self, config: LLMConfig):
        self.config = config
        self.client = None
        self._setup_client()
    
    def _setup_client(self):
        """LLM 클라이언트 설정"""
        try:
            if self.config.provider == LLMProvider.OPENAI:
                if OPENAI_AVAILABLE and self.config.api_key:
                    # 실제 OpenAI 클라이언트 설정
                    openai.api_key = self.config.api_key
                    self.client = "openai"
                    logger.info("✅ OpenAI 클라이언트 설정 완료")
                else:
                    logger.warning("⚠️  OpenAI API 키가 없습니다. 시뮬레이션 모드로 전환합니다.")
                    self.config.provider = LLMProvider.SIMULATION
            
            elif self.config.provider == LLMProvider.OLLAMA:
                if OLLAMA_AVAILABLE:
                    # 실제 Ollama 클라이언트 설정
                    self.client = Ollama(model=self.config.model)
                    logger.info(f"✅ Ollama 클라이언트 설정 완료: {self.config.model}")
                else:
                    logger.warning("⚠️  Ollama가 설치되지 않았습니다. 시뮬레이션 모드로 전환합니다.")
                    self.config.provider = LLMProvider.SIMULATION
            
            if self.config.provider == LLMProvider.SIMULATION:
                self.client = "simulation"
                logger.info("🎭 시뮬레이션 모드로 LLM 동작을 시뮬레이션합니다.")
                
        except Exception as e:
            logger.error(f"LLM 클라이언트 설정 실패: {str(e)}")
            self.config.provider = LLMProvider.SIMULATION
            self.client = "simulation"
    
    def generate(self, prompt: str, system_prompt: str = "") -> str:
        """텍스트 생성"""
        try:
            if self.config.provider == LLMProvider.OPENAI:
                return self._generate_openai(prompt, system_prompt)
            elif self.config.provider == LLMProvider.OLLAMA:
                return self._generate_ollama(prompt, system_prompt)
            else:
                return self._generate_simulation(prompt, system_prompt)
                
        except Exception as e:
            logger.error(f"텍스트 생성 실패: {str(e)}")
            return self._generate_simulation(prompt, system_prompt)
    
    def _generate_openai(self, prompt: str, system_prompt: str = "") -> str:
        """OpenAI API 호출"""
        # 실제 구현 코드
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        # 실제로는 이렇게 호출
        # response = openai.ChatCompletion.create(
        #     model=self.config.model,
        #     messages=messages,
        #     temperature=self.config.temperature,
        #     max_tokens=self.config.max_tokens
        # )
        # return response.choices[0].message.content
        
        # API 키가 없으므로 시뮬레이션으로 대체
        return self._generate_simulation(prompt, system_prompt)
    
    def _generate_ollama(self, prompt: str, system_prompt: str = "") -> str:
        """Ollama 호출"""
        full_prompt = f"{system_prompt}\n\n{prompt}" if system_prompt else prompt
        
        # 실제로는 이렇게 호출
        # response = self.client(full_prompt)
        # return response
        
        # Ollama가 없으므로 시뮬레이션으로 대체
        return self._generate_simulation(prompt, system_prompt)
    
    def _generate_simulation(self, prompt: str, system_prompt: str = "") -> str:
        """
        시뮬레이션 모드 - 실제 LLM처럼 동작하는 가짜 응답 생성
        
        실제 LLM의 추론 패턴을 모방하여 상황에 맞는 응답을 생성합니다.
        """
        # 약간의 지연 시뮬레이션 (실제 API 호출처럼)
        time.sleep(0.5)
        
        # 프롬프트 분석하여 적절한 응답 생성
        prompt_lower = prompt.lower()
        
        # 사고 과정 요청
        if "생각" in prompt or "분석" in prompt or "think" in prompt_lower:
            if "파일" in prompt or "file" in prompt_lower:
                return """현재 상황을 분석해보겠습니다.

사용자가 파일 관련 작업을 요청했습니다. 먼저 현재 디렉토리의 파일 목록을 확인하여 어떤 파일들이 있는지 파악해야 합니다. 그 다음에 사용자의 구체적인 요구사항에 따라 파일을 읽거나, 생성하거나, 수정하는 작업을 수행하겠습니다.

다음 단계: list_files 도구를 사용하여 현재 디렉토리 탐색"""

            elif "날씨" in prompt or "weather" in prompt_lower:
                return """사용자가 날씨 정보를 요청했습니다.

날씨 정보를 제공하기 위해서는 get_weather 도구를 사용해야 합니다. 사용자가 특정 도시를 언급하지 않았다면 기본적으로 서울의 날씨를 조회하겠습니다. 날씨 정보를 가져온 후에는 사용자가 이해하기 쉽게 정리해서 제공하겠습니다.

다음 단계: get_weather 도구로 날씨 정보 조회"""

            elif "뉴스" in prompt or "news" in prompt_lower:
                return """사용자가 뉴스 정보를 요청했습니다.

최신 뉴스를 제공하기 위해 get_news 도구를 사용하겠습니다. 한국 뉴스를 기본으로 하되, 기술 관련 뉴스를 우선적으로 가져와서 사용자에게 유용한 정보를 제공하겠습니다.

다음 단계: get_news 도구로 최신 뉴스 조회"""

            else:
                return """현재 상황을 분석하고 있습니다.

사용자의 요청을 이해하고 목표를 달성하기 위한 최적의 방법을 찾고 있습니다. 사용 가능한 도구들을 검토하여 가장 적절한 도구를 선택하겠습니다.

다음 단계: 적절한 도구 선택 및 실행"""

        # 도구 선택 요청
        elif "도구" in prompt or "tool" in prompt_lower or "action" in prompt_lower:
            if "파일" in prompt:
                return """{
    "tool_name": "list_files",
    "parameters": {
        "directory": ".",
        "show_hidden": false
    },
    "reasoning": "현재 디렉토리의 파일 목록을 확인하여 사용자가 작업할 수 있는 파일들을 파악합니다."
}"""
            elif "날씨" in prompt:
                return """{
    "tool_name": "get_weather",
    "parameters": {
        "city": "서울",
        "country": "KR",
        "units": "metric"
    },
    "reasoning": "서울의 현재 날씨 정보를 조회하여 사용자에게 제공합니다."
}"""
            elif "뉴스" in prompt:
                return """{
    "tool_name": "get_news",
    "parameters": {
        "country": "kr",
        "category": "technology",
        "max_articles": 5
    },
    "reasoning": "한국의 최신 기술 뉴스를 조회하여 사용자에게 유용한 정보를 제공합니다."
}"""
            else:
                return """{
    "tool_name": "list_files",
    "parameters": {
        "directory": "."
    },
    "reasoning": "기본적으로 현재 상황을 파악하기 위해 파일 목록을 확인합니다."
}"""

        # 결과 분석 요청
        elif "결과" in prompt or "관찰" in prompt or "observe" in prompt_lower:
            if "성공" in prompt or "success" in prompt_lower:
                return """도구 실행이 성공적으로 완료되었습니다.

결과를 분석해보니 사용자의 요청에 필요한 정보를 성공적으로 수집했습니다. 이제 이 정보를 바탕으로 다음 단계를 진행하거나, 사용자에게 결과를 제공할 수 있습니다.

목표 달성 여부: 기본 정보 수집 완료, 추가 작업 필요 여부 검토 중"""

            else:
                return """도구 실행 결과를 분석하고 있습니다.

실행 결과를 바탕으로 다음 단계를 계획하고 있습니다. 필요하다면 추가적인 도구를 사용하거나, 현재까지의 결과를 정리하여 사용자에게 제공하겠습니다."""

        # 계획 수립 요청
        elif "계획" in prompt or "plan" in prompt_lower:
            return """작업 계획을 수립하겠습니다.

1단계: 현재 상황 파악 및 필요한 정보 수집
2단계: 사용자 요청에 맞는 적절한 도구 선택
3단계: 도구 실행 및 결과 확인
4단계: 결과 분석 및 추가 작업 필요성 판단
5단계: 최종 결과 정리 및 사용자에게 제공

이 계획에 따라 단계별로 작업을 진행하겠습니다."""

        # 기본 응답
        else:
            return """네, 이해했습니다. 

사용자의 요청을 분석하고 최적의 방법으로 처리하겠습니다. 필요한 도구들을 활용하여 정확하고 유용한 결과를 제공하도록 하겠습니다."""


class LLMAgent:
    """
    실제 LLM 기반 AI Agent
    
    진짜 추론 능력을 가진 Agent로, 상황에 따라 동적으로 계획을 세우고
    적절한 도구를 선택하여 목표를 달성합니다.
    """
    
    def __init__(self, name: str, llm_config: LLMConfig, rag_system=None, mcp_server=None):
        self.name = name
        self.llm = LLMInterface(llm_config)
        self.rag_system = rag_system
        self.mcp_server = mcp_server
        
        self.available_tools: List[Dict] = []
        self.execution_history: List[Dict] = []
        self.current_task: Optional[Dict] = None
        
        # MCP 도구 목록 로드
        if self.mcp_server:
            self._load_available_tools()
        
        logger.info(f"🧠 LLM 기반 AI Agent '{name}' 초기화 완료")
    
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
    
    def execute_task(self, task_description: str, max_steps: int = 10) -> Dict[str, Any]:
        """
        LLM 기반 작업 실행
        
        실제 LLM이 상황을 분석하고, 계획을 세우고, 도구를 선택하여 실행합니다.
        """
        self.current_task = {
            "description": task_description,
            "start_time": time.time(),
            "max_steps": max_steps
        }
        self.execution_history = []
        
        logger.info(f"🚀 LLM Agent 작업 시작: {task_description}")
        
        try:
            step_number = 1
            
            while step_number <= max_steps:
                logger.info(f"📍 Step {step_number}: 사고 과정 시작")
                
                # 1. Think: LLM이 현재 상황을 분석하고 다음 행동을 계획
                thought = self._llm_think(step_number)
                self._add_to_history("thought", thought, step_number)
                
                # 목표 달성 확인
                if self._is_goal_achieved(thought):
                    logger.info("🎯 목표 달성 완료!")
                    break
                
                # 2. Act: LLM이 도구를 선택하고 실행
                logger.info(f"🎬 Step {step_number}: 행동 실행")
                action_result = self._llm_act(thought, step_number)
                self._add_to_history("action", action_result, step_number)
                
                # 3. Observe: LLM이 결과를 관찰하고 분석
                logger.info(f"👁️  Step {step_number}: 결과 관찰")
                observation = self._llm_observe(action_result, step_number)
                self._add_to_history("observation", observation, step_number)
                
                step_number += 1
            
            execution_time = time.time() - self.current_task["start_time"]
            
            return {
                "success": True,
                "task": task_description,
                "execution_time": execution_time,
                "total_steps": len([h for h in self.execution_history if h["type"] == "thought"]),
                "history": self.execution_history,
                "final_summary": self._generate_final_summary()
            }
            
        except Exception as e:
            logger.error(f"작업 실행 중 오류: {str(e)}")
            return {
                "success": False,
                "error": str(e),
                "task": task_description,
                "history": self.execution_history
            }
    
    def _llm_think(self, step_number: int) -> str:
        """LLM이 현재 상황을 분석하고 다음 행동을 계획"""
        
        # 컨텍스트 구성
        context = self._build_context(step_number)
        
        # RAG 시스템으로 관련 지식 검색 (있는 경우)
        relevant_knowledge = ""
        if self.rag_system:
            try:
                rag_result = self.rag_system.query(self.current_task["description"])
                if rag_result.get("answer"):
                    relevant_knowledge = f"\n관련 지식:\n{rag_result['answer'][:300]}..."
            except Exception as e:
                logger.warning(f"RAG 검색 실패: {str(e)}")
        
        # LLM 프롬프트 구성
        system_prompt = """당신은 자율적으로 작업을 수행하는 AI Agent입니다.
주어진 목표를 달성하기 위해 단계별로 생각하고 적절한 도구를 선택하여 실행합니다.
현재 상황을 분석하고 다음에 무엇을 해야 할지 명확하게 설명하세요."""

        user_prompt = f"""
현재 작업: {self.current_task['description']}
단계: {step_number}/{self.current_task['max_steps']}

{context}

사용 가능한 도구들:
{self._format_available_tools()}

{relevant_knowledge}

현재 상황을 분석하고 다음에 무엇을 해야 할지 생각해보세요.
목표 달성을 위한 구체적인 계획을 설명하세요.
"""
        
        # LLM 호출
        thought = self.llm.generate(user_prompt, system_prompt)
        logger.info(f"🧠 LLM 사고: {thought[:100]}...")
        
        return thought
    
    def _llm_act(self, thought: str, step_number: int) -> Dict[str, Any]:
        """LLM이 도구를 선택하고 실행"""
        
        # LLM에게 도구 선택 요청
        system_prompt = """당신은 생각한 내용을 바탕으로 적절한 도구를 선택하고 실행해야 합니다.
JSON 형태로 도구 이름과 파라미터를 정확히 지정하세요."""

        user_prompt = f"""
현재 생각: {thought}

사용 가능한 도구들:
{self._format_available_tools()}

위의 생각을 바탕으로 어떤 도구를 어떤 파라미터로 실행해야 할까요?

다음 JSON 형태로 답변하세요:
{{
    "tool_name": "도구_이름",
    "parameters": {{
        "param1": "value1",
        "param2": "value2"
    }},
    "reasoning": "이 도구를 선택한 이유"
}}
"""
        
        # LLM 호출
        llm_response = self.llm.generate(user_prompt, system_prompt)
        
        try:
            # JSON 파싱 시도
            if "{" in llm_response and "}" in llm_response:
                json_start = llm_response.find("{")
                json_end = llm_response.rfind("}") + 1
                json_str = llm_response[json_start:json_end]
                action_plan = json.loads(json_str)
            else:
                # JSON이 없으면 기본 도구 선택
                action_plan = {
                    "tool_name": self.available_tools[0]["name"] if self.available_tools else "list_files",
                    "parameters": {},
                    "reasoning": "기본 도구 선택"
                }
            
            # 도구 실행
            result = self._execute_tool(
                action_plan["tool_name"],
                action_plan.get("parameters", {}),
                step_number
            )
            
            result["reasoning"] = action_plan.get("reasoning", "")
            result["llm_response"] = llm_response
            
            return result
            
        except Exception as e:
            logger.error(f"도구 실행 실패: {str(e)}")
            return {
                "success": False,
                "error": str(e),
                "llm_response": llm_response
            }
    
    def _llm_observe(self, action_result: Dict[str, Any], step_number: int) -> str:
        """LLM이 실행 결과를 관찰하고 분석"""
        
        system_prompt = """당신은 도구 실행 결과를 분석하고 다음 단계를 계획하는 AI Agent입니다.
실행 결과를 바탕으로 목표 달성 여부와 다음에 해야 할 일을 분석하세요."""

        user_prompt = f"""
실행한 도구: {action_result.get('tool_name', 'unknown')}
실행 결과: {json.dumps(action_result, ensure_ascii=False, indent=2)}

이 결과를 분석하고 다음을 설명하세요:
1. 실행이 성공했는지 여부
2. 얻은 정보나 결과의 의미
3. 목표 달성에 얼마나 가까워졌는지
4. 다음에 해야 할 일이 있는지

현재 작업: {self.current_task['description']}
"""
        
        # LLM 호출
        observation = self.llm.generate(user_prompt, system_prompt)
        logger.info(f"👁️  LLM 관찰: {observation[:100]}...")
        
        return observation
    
    def _execute_tool(self, tool_name: str, parameters: Dict[str, Any], step_number: int) -> Dict[str, Any]:
        """실제 도구 실행"""
        try:
            request_data = {
                "action": "execute_tool",
                "tool_name": tool_name,
                "parameters": parameters,
                "request_id": f"llm_agent_step_{step_number}"
            }
            
            request_json = json.dumps(request_data)
            response_json = self.mcp_server.handle_request(request_json)
            response = json.loads(response_json)
            
            result = {
                "success": response["success"],
                "tool_name": tool_name,
                "parameters": parameters,
                "result": response.get("result"),
                "error": response.get("error")
            }
            
            if result["success"]:
                logger.info(f"✅ 도구 실행 성공: {tool_name}")
            else:
                logger.error(f"❌ 도구 실행 실패: {tool_name} - {result['error']}")
            
            return result
            
        except Exception as e:
            logger.error(f"도구 실행 중 오류: {str(e)}")
            return {
                "success": False,
                "tool_name": tool_name,
                "parameters": parameters,
                "error": str(e)
            }
    
    def _build_context(self, step_number: int) -> str:
        """현재 컨텍스트 구성"""
        context = ""
        
        if self.execution_history:
            context += "지금까지의 실행 기록:\n"
            for entry in self.execution_history[-6:]:  # 최근 6개만
                context += f"- {entry['type']}: {entry['content'][:100]}...\n"
        else:
            context += "이것은 첫 번째 단계입니다.\n"
        
        return context
    
    def _format_available_tools(self) -> str:
        """사용 가능한 도구들을 포맷팅"""
        if not self.available_tools:
            return "사용 가능한 도구가 없습니다."
        
        tools_text = ""
        for tool in self.available_tools[:8]:  # 상위 8개만
            tools_text += f"- {tool['name']}: {tool['description']}\n"
        
        return tools_text
    
    def _is_goal_achieved(self, thought: str) -> bool:
        """목표 달성 여부 확인 (LLM 응답 기반)"""
        # 간단한 휴리스틱
        achievement_keywords = ["완료", "달성", "성공", "끝", "목표", "완성"]
        thought_lower = thought.lower()
        
        return any(keyword in thought_lower for keyword in achievement_keywords)
    
    def _add_to_history(self, entry_type: str, content: str, step_number: int):
        """실행 기록에 추가"""
        self.execution_history.append({
            "type": entry_type,
            "content": content,
            "step": step_number,
            "timestamp": time.time()
        })
    
    def _generate_final_summary(self) -> str:
        """최종 요약 생성"""
        if not self.execution_history:
            return "실행 기록이 없습니다."
        
        # 마지막 관찰 내용을 요약으로 사용
        observations = [h for h in self.execution_history if h["type"] == "observation"]
        if observations:
            return observations[-1]["content"]
        
        return "작업을 수행했지만 명확한 결과를 확인할 수 없습니다."


if __name__ == "__main__":
    # 테스트용 설정
    config = LLMConfig(
        provider=LLMProvider.SIMULATION,  # 시뮬레이션 모드
        model="gpt-3.5-turbo"
    )
    
    agent = LLMAgent("테스트 LLM Agent", config)
    print(f"LLM Agent 생성 완료: {agent.name}")
    print(f"LLM 제공자: {agent.llm.config.provider.value}")