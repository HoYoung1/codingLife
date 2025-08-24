"""
웹 API 호출 MCP 도구들

실제 외부 API들을 호출하는 MCP 도구들을 구현합니다.
이것이 실제 Gmail MCP, Slack MCP 등이 하는 일과 비슷합니다.
"""

import requests
import json
from typing import Dict, Any, List
import logging

logger = logging.getLogger(__name__)


class WeatherMCPTools:
    """
    날씨 API를 MCP 도구로 래핑한 예시
    
    실제로는 OpenWeatherMap API를 호출하지만,
    LLM에게는 간단한 인터페이스만 제공
    """
    
    def __init__(self, api_key: str = "demo_key"):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5"
    
    def get_current_weather(self, city: str, country: str = "", units: str = "metric") -> Dict[str, Any]:
        """
        현재 날씨 조회
        
        LLM이 보는 것: 간단한 함수 호출
        실제로 하는 일: API 호출 + 데이터 정리 + 에러 처리
        """
        try:
            # 1. 파라미터 정리
            location = f"{city},{country}" if country else city
            
            # 2. API 호출
            url = f"{self.base_url}/weather"
            params = {
                "q": location,
                "appid": self.api_key,
                "units": units,
                "lang": "kr"
            }
            
            # 실제 환경에서는 실제 API 호출
            # response = requests.get(url, params=params)
            
            # 데모용 가짜 응답
            fake_response = {
                "weather": [{"main": "Clear", "description": "맑음"}],
                "main": {"temp": 22.5, "feels_like": 25.0, "humidity": 60},
                "wind": {"speed": 3.2},
                "name": city
            }
            
            # 3. LLM이 이해하기 쉽게 데이터 변환
            return {
                "success": True,
                "location": fake_response["name"],
                "temperature": f"{fake_response['main']['temp']}°C",
                "feels_like": f"{fake_response['main']['feels_like']}°C",
                "description": fake_response["weather"][0]["description"],
                "humidity": f"{fake_response['main']['humidity']}%",
                "wind_speed": f"{fake_response['wind']['speed']} m/s",
                "summary": f"{city}의 현재 날씨는 {fake_response['weather'][0]['description']}이며, 기온은 {fake_response['main']['temp']}°C입니다."
            }
            
        except Exception as e:
            logger.error(f"날씨 조회 실패: {str(e)}")
            return {
                "success": False,
                "error": f"날씨 정보를 가져올 수 없습니다: {str(e)}"
            }


class NewsAPIMCPTools:
    """
    뉴스 API를 MCP 도구로 래핑한 예시
    """
    
    def __init__(self, api_key: str = "demo_key"):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2"
    
    def get_top_headlines(self, country: str = "kr", category: str = "", max_articles: int = 5) -> Dict[str, Any]:
        """
        주요 뉴스 헤드라인 조회
        
        실제로는 NewsAPI 호출하지만, LLM에게는 정리된 결과만 제공
        """
        try:
            # 데모용 가짜 뉴스 데이터
            fake_articles = [
                {
                    "title": "AI 기술 발전으로 새로운 일자리 창출",
                    "description": "인공지능 기술의 발전이 새로운 형태의 일자리를 만들어내고 있다.",
                    "url": "https://example.com/news1",
                    "publishedAt": "2024-01-15T10:00:00Z",
                    "source": {"name": "테크뉴스"}
                },
                {
                    "title": "MCP 프로토콜, LLM과 시스템 연결의 새로운 표준",
                    "description": "Model Context Protocol이 AI 에이전트 개발의 핵심 기술로 주목받고 있다.",
                    "url": "https://example.com/news2", 
                    "publishedAt": "2024-01-15T09:30:00Z",
                    "source": {"name": "AI타임즈"}
                }
            ]
            
            # LLM이 이해하기 쉽게 정리
            articles = []
            for article in fake_articles[:max_articles]:
                articles.append({
                    "title": article["title"],
                    "summary": article["description"],
                    "source": article["source"]["name"],
                    "url": article["url"],
                    "published": article["publishedAt"][:10]  # 날짜만
                })
            
            return {
                "success": True,
                "country": country,
                "category": category or "전체",
                "total_articles": len(articles),
                "articles": articles,
                "summary": f"{country} 지역의 주요 뉴스 {len(articles)}건을 가져왔습니다."
            }
            
        except Exception as e:
            logger.error(f"뉴스 조회 실패: {str(e)}")
            return {
                "success": False,
                "error": f"뉴스를 가져올 수 없습니다: {str(e)}"
            }


class SlackMCPTools:
    """
    Slack API를 MCP 도구로 래핑한 예시
    
    실제 Slack MCP는 이런 식으로 구현됩니다.
    """
    
    def __init__(self, bot_token: str = "demo_token"):
        self.bot_token = bot_token
        self.base_url = "https://slack.com/api"
    
    def send_message(self, channel: str, text: str, username: str = "AI Assistant") -> Dict[str, Any]:
        """
        Slack 메시지 전송
        
        LLM: "슬랙에 메시지 보내줘"
        MCP: Slack API 호출 + 결과 정리
        """
        try:
            # 실제로는 Slack API 호출
            # headers = {"Authorization": f"Bearer {self.bot_token}"}
            # data = {"channel": channel, "text": text, "username": username}
            # response = requests.post(f"{self.base_url}/chat.postMessage", headers=headers, data=data)
            
            # 데모용 가짜 응답
            fake_response = {
                "ok": True,
                "channel": channel,
                "ts": "1234567890.123456",
                "message": {
                    "text": text,
                    "username": username
                }
            }
            
            return {
                "success": True,
                "channel": channel,
                "message": text,
                "timestamp": fake_response["ts"],
                "summary": f"#{channel} 채널에 메시지를 성공적으로 전송했습니다."
            }
            
        except Exception as e:
            logger.error(f"Slack 메시지 전송 실패: {str(e)}")
            return {
                "success": False,
                "error": f"메시지 전송에 실패했습니다: {str(e)}"
            }
    
    def get_channels(self) -> Dict[str, Any]:
        """
        Slack 채널 목록 조회
        """
        try:
            # 데모용 가짜 채널 목록
            fake_channels = [
                {"id": "C1234567890", "name": "general", "is_member": True},
                {"id": "C2345678901", "name": "random", "is_member": True},
                {"id": "C3456789012", "name": "ai-development", "is_member": False}
            ]
            
            channels = []
            for channel in fake_channels:
                channels.append({
                    "name": channel["name"],
                    "id": channel["id"],
                    "member": "참여중" if channel["is_member"] else "미참여"
                })
            
            return {
                "success": True,
                "total_channels": len(channels),
                "channels": channels,
                "summary": f"총 {len(channels)}개의 채널을 찾았습니다."
            }
            
        except Exception as e:
            logger.error(f"채널 목록 조회 실패: {str(e)}")
            return {
                "success": False,
                "error": f"채널 목록을 가져올 수 없습니다: {str(e)}"
            }


# MCP 도구 정의들
WEB_API_TOOLS = [
    {
        "name": "get_weather",
        "description": "지정된 도시의 현재 날씨 정보를 조회합니다",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "날씨를 조회할 도시명"
                },
                "country": {
                    "type": "string", 
                    "description": "국가 코드 (선택사항, 예: KR, US)",
                    "default": ""
                },
                "units": {
                    "type": "string",
                    "description": "온도 단위 (metric, imperial, kelvin)",
                    "default": "metric"
                }
            },
            "required": ["city"]
        },
        "function": lambda city, country="", units="metric": WeatherMCPTools().get_current_weather(city, country, units)
    },
    {
        "name": "get_news",
        "description": "최신 뉴스 헤드라인을 조회합니다",
        "parameters": {
            "type": "object",
            "properties": {
                "country": {
                    "type": "string",
                    "description": "국가 코드 (kr, us, jp 등)",
                    "default": "kr"
                },
                "category": {
                    "type": "string",
                    "description": "뉴스 카테고리 (technology, business, sports 등)",
                    "default": ""
                },
                "max_articles": {
                    "type": "integer",
                    "description": "가져올 기사 수 (최대 10개)",
                    "default": 5
                }
            },
            "required": []
        },
        "function": lambda country="kr", category="", max_articles=5: NewsAPIMCPTools().get_top_headlines(country, category, max_articles)
    },
    {
        "name": "send_slack_message",
        "description": "Slack 채널에 메시지를 전송합니다",
        "parameters": {
            "type": "object",
            "properties": {
                "channel": {
                    "type": "string",
                    "description": "메시지를 보낼 채널명 (# 없이)"
                },
                "text": {
                    "type": "string",
                    "description": "전송할 메시지 내용"
                },
                "username": {
                    "type": "string",
                    "description": "발신자 이름",
                    "default": "AI Assistant"
                }
            },
            "required": ["channel", "text"]
        },
        "function": lambda channel, text, username="AI Assistant": SlackMCPTools().send_message(channel, text, username)
    },
    {
        "name": "get_slack_channels",
        "description": "Slack 워크스페이스의 채널 목록을 조회합니다",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        },
        "function": lambda: SlackMCPTools().get_channels()
    }
]


if __name__ == "__main__":
    # 웹 API 도구들 테스트
    print("=== 웹 API MCP 도구들 테스트 ===")
    
    # 1. 날씨 조회
    print("\n1. 날씨 조회:")
    weather_tool = WeatherMCPTools()
    result = weather_tool.get_current_weather("서울", "KR")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    
    # 2. 뉴스 조회
    print("\n2. 뉴스 조회:")
    news_tool = NewsAPIMCPTools()
    result = news_tool.get_top_headlines("kr", "", 3)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    
    # 3. Slack 메시지 전송
    print("\n3. Slack 메시지 전송:")
    slack_tool = SlackMCPTools()
    result = slack_tool.send_message("general", "MCP 테스트 메시지입니다!")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    
    # 4. Slack 채널 목록
    print("\n4. Slack 채널 목록:")
    result = slack_tool.get_channels()
    print(json.dumps(result, ensure_ascii=False, indent=2))