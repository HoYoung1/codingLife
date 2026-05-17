PRD

[서비스명: Semi-Quality Sentinel (A2A 기반 품질 전조 증상 분석기)]
1. 프로젝트 개요
1.1 프로젝트 기획 배경
* 문제 정의: 현재 반도체 공정 품질 관리는 운영자가 차트를 직접 모니터링하거나 단순 임계치 알람(Limit Out)에 의존하고 있어, 수치 이면의 맥락(Context) 파악이 늦음.
* 한계: 단순 알람은 이미 불량이 발생한 후의 사후 대응인 경우가 많으며, 장비 정비(PM) 등 외부 이벤트와의 상관관계를 즉각적으로 분석하기 어려움.
* 해결책: 멀티 에이전트가 로그 분석, 매뉴얼 대조, 대응 전략 수립을 분담하여 '전조 증상'을 감지하고 선제적 조치를 제안함.
1.2 핵심 아이디어 및 가치 제안(Value Proposition)
* 핵심 기능: 텍스트 기반 공정 로그 실시간 스캔 및 에이전트 간 협업을 통한 이상 원인 추론.
* 기대 효과: 불량 발생 전 가동 중단(Down-time) 최소화 및 숙련된 엔지니어 수준의 원인 분석 리포트 자동 생성.
* 차별성: 단순 수치 비교를 넘어 "정비 이후의 추세 변화"라는 시계열 맥락 분석 수행.
1.3 대상 사용자 및 기대 사용자 경험(UX)
* 주요 타겟: 반도체 품질 관리 엔지니어 및 생산 라인 운영자.
* 사용자 경험: 대시보드에 로그를 입력하거나 실시간 스트리밍 시, 에이전트들이 "토론"하여 도출한 분석 결과와 조치 권고안을 한눈에 확인.

2. 기술 구성
2.1 Prompt Engineering 전략
* 역할 기반: 각 에이전트(Analyzer, Expert, Strategist)에 명확한 페르소나 부여.
* CoT(Chain of Thought): 수치 변화 → 과거 이벤트 대조 → 인과 추론으로 이어지는 사고 과정 유도.
* 출력 구조화: JSON 형태의 구조화된 출력을 통해 UI(Streamlit) 시각화 용이성 확보.
2.2 LangChain / LangGraph 기반 Agent 구조
* Multi-Agent 설계:
    1. Log Analyzer Agent: 텍스트 로그에서 트렌드(우상향 등) 및 이상치 추출.
    2. Standard Expert Agent (RAG): 공정 표준서 및 장비 매뉴얼(가상 데이터)을 참조하여 현재 상태 판단.
    3. Strategy Response Agent: 최종 대응 시나리오 및 운영자 보고서 작성.
* Collaboration: LangGraph의 State를 공유하며 Analyzer의 결과물을 바탕으로 Expert가 조언하는 순차적/반복적 구조.
2.3 RAG 구성
* 데이터: 가상의 장비 운영 매뉴얼(PDF/TXT) 및 표준 공정 규격서.
* Vector DB: FAISS 또는 Chroma를 사용한 로컬 인덱싱.
2.4 서비스 개발 및 패키징 계획
* UI: Streamlit을 사용하여 로그 입력 창 및 에이전트 간 대화 로그 시각화.
* BE: FastAPI 기반의 비동기 에이전트 호출 구조.
* 환경: Docker 기반 컨테이너화 (선택 사항).

3. 주요 기능 및 동작 시나리오
3.1 사용자 시나리오(Use Case Scenario)
1. 입력: 운영자가 텍스트 형태의 장비 로그(PM 기록 포함)를 시스템에 입력.
2. 분석: Analyzer가 "PM 이후 파티클 수치 미세 우상향" 패턴 포착.
3. 협업: Expert가 "PM 이후 세정 미흡 시 발생 가능한 현상"임을 RAG로 검색하여 확인.
4. 출력: Strategist가 "장비 일시 중단 및 재세정 권고" 리포트 생성.
3.2 시스템 구조도 (Multi-Agent Diagram 개념)
코드 스니펫

graph LR
    Log[Text Log Data] --> A[Log Analyzer Agent]
    A --> |Detect Trend| E[Standard Expert Agent]
    R[(RAG: Manuals)] --> E
    E --> |Consultation| S[Strategy Response Agent]
    S --> UI[Streamlit UI / Report]

4. 구현을 위한 가상 데이터 샘플 (텍스트 로그형)
Plaintext

[2026-05-13 09:00] EVENT: Preventive Maintenance (PM) Completed. Operator: Kim.
[2026-05-14 10:00] SENSOR_PARTICLE: 0.012 (Status: Normal)
[2026-05-14 11:00] SENSOR_PARTICLE: 0.015 (Status: Normal)
[2026-05-14 12:00] SENSOR_PARTICLE: 0.018 (Status: Warning - Slight Upward Drift)
[2026-05-14 13:00] SENSOR_PARTICLE: 0.021 (Status: Warning - Trend Detected)

