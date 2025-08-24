# Kafka 학습 프로젝트

AWS Kinesis 경험을 바탕으로 Apache Kafka를 단계별로 학습하는 프로젝트입니다.

## 학습 목표
- Kafka 핵심 개념 이해 (Topic, Partition, Producer, Consumer)
- Zookeeper 역할과 KRaft 모드 차이점 학습
- Python으로 실제 Producer/Consumer 구현
- 실시간 데이터 처리 파이프라인 구축

## 학습 단계

### 1단계: 기초 이론 + 환경 구축 ✅
- [x] Kafka vs Kinesis 비교 이해
- [x] Docker로 Kafka 클러스터 구축
- [x] Kafka CLI 도구 사용법
- [x] Consumer Group과 오프셋 개념 이해
- [x] 실무 모니터링 명령어 학습

### 2단계: Python 기초 실습
- [x] kafka-python 라이브러리 사용
- [x] 간단한 Producer/Consumer 구현
- [ ] 메시지 직렬화 처리 (JSON, Avro)
- [ ] 에러 처리와 재시도 로직
- [ ] 배치 처리 최적화

### 3단계: 실전 프로젝트
- [ ] 실시간 로그 처리 시스템
- [ ] 마이크로서비스 이벤트 통신
- [ ] 스트림 처리 (Kafka Streams)
- [ ] 스키마 레지스트리 활용

## 환경 요구사항
- Python 3.8+
- Docker & Docker Compose
- kafka-python 라이브러리
## 오늘
 학습한 내용 (완료)

### 핵심 개념 이해
- Kafka vs AWS Kinesis 비교
- Topic, Partition, Producer, Consumer 개념
- Zookeeper 역할과 KRaft 모드
- Consumer Group과 오프셋 관리

### 실습 환경 구축
- Docker Compose로 Kafka 클러스터 구축
- Kafka UI를 통한 시각적 모니터링
- Python Producer/Consumer 기본 구현

### CLI 명령어 마스터
- 토픽 조회 및 관리
- 메시지 조회 (Consumer에 영향 없이)
- Consumer Group 상태 모니터링
- Lag 분석 및 오프셋 관리

### 실무 시나리오 대응
- Consumer 문제 상황별 대응법
- 모니터링 체크리스트
- 상태 체크 자동화 스크립트

## 다음 학습 계획

### 우선순위 1: 메시지 처리 고도화
1. **메시지 직렬화/역직렬화**
   - JSON vs Avro vs Protobuf 비교
   - 스키마 진화 (Schema Evolution)
   - 스키마 레지스트리 사용법

2. **에러 처리 및 안정성**
   - Dead Letter Queue 패턴
   - 재시도 로직 구현
   - 멱등성 보장 방법

### 우선순위 2: 성능 최적화
1. **Producer 최적화**
   - 배치 처리 설정
   - 압축 옵션
   - 파티셔닝 전략

2. **Consumer 최적화**
   - 병렬 처리 패턴
   - 커밋 전략
   - 메모리 관리

### 우선순위 3: 실전 프로젝트
1. **실시간 이벤트 처리 시스템**
   - 사용자 행동 로그 수집
   - 실시간 집계 및 알림
   - 대시보드 연동

2. **마이크로서비스 통신**
   - 이벤트 소싱 패턴
   - SAGA 패턴 구현
   - 분산 트랜잭션 처리

## 유용한 리소스

### 문서
- [docs/01-kafka-basics.md](docs/01-kafka-basics.md) - 기초 개념
- [docs/03-kafka-cli-commands.md](docs/03-kafka-cli-commands.md) - CLI 명령어 가이드
- [docs/04-consumer-only-workflow.md](docs/04-consumer-only-workflow.md) - Consumer 전용 워크플로우
- [docs/05-real-world-scenarios.md](docs/05-real-world-scenarios.md) - 실무 시나리오

### 스크립트
- [scripts/kafka-health-check.sh](scripts/kafka-health-check.sh) - 상태 체크 자동화