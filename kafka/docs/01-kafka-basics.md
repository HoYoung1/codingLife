# Kafka 기초 개념

## Kafka vs AWS Kinesis 비교

이미 Kinesis를 써봤으니 비교해서 이해해보자:

| 개념 | AWS Kinesis | Apache Kafka |
|------|-------------|--------------|
| 스트림 | Kinesis Stream | Topic |
| 샤드 | Shard | Partition |
| 레코드 | Record | Message/Event |
| 프로듀서 | Producer | Producer |
| 컨슈머 | Consumer | Consumer |

## Kafka 핵심 개념

### 1. Topic (토픽)
- Kinesis의 Stream과 비슷한 개념
- 메시지들이 저장되는 논리적 채널
- 예: `user-events`, `order-logs`, `payment-notifications`

### 2. Partition (파티션)
- Kinesis의 Shard와 비슷
- Topic을 물리적으로 나눈 단위
- 병렬 처리와 확장성을 위해 사용
- 각 파티션은 순서가 보장됨

### 3. Producer (프로듀서)
- 메시지를 Topic에 발행하는 클라이언트
- 어떤 파티션에 보낼지 결정 (키 기반 또는 라운드로빈)

### 4. Consumer (컨슈머)
- Topic에서 메시지를 읽는 클라이언트
- Consumer Group으로 묶어서 병렬 처리 가능

### 5. Broker (브로커)
- Kafka 서버 인스턴스
- 여러 브로커가 클러스터를 구성

## Zookeeper란?

**기존 역할:**
- 브로커들의 메타데이터 관리
- 리더 파티션 선출
- 클러스터 구성 정보 저장

**최신 동향:**
- Kafka 2.8부터 KRaft 모드 도입
- Zookeeper 없이도 동작 가능
- 더 간단한 운영과 더 나은 성능

우리는 학습용이니 Docker Compose로 간단하게 구축해보자!