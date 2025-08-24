# Consumer 전용 시스템에서의 Kafka 접근법

## 상황 이해

**당신의 상황:**
- 다른 팀이 Producer 역할 (메시지 생산)
- 당신의 시스템은 Consumer 역할 (메시지 소비)
- Kafka 초보자로서 기본적인 모니터링과 디버깅 필요

## 1. 기본 정보 파악하기

### 먼저 알아야 할 것들
```bash
# 1. 어떤 토픽들이 있는지 확인
docker exec kafka kafka-topics --list --bootstrap-server localhost:9092

# 2. 내가 사용할 토픽의 구조 파악
docker exec kafka kafka-topics --describe --topic [토픽명] --bootstrap-server localhost:9092
```

### 토픽 구조 이해하기
```
Topic: user-events  PartitionCount: 3  ReplicationFactor: 1
  Topic: user-events  Partition: 0  Leader: 1  Replicas: 1  Isr: 1
  Topic: user-events  Partition: 1  Leader: 1  Replicas: 1  Isr: 1
  Topic: user-events  Partition: 2  Leader: 1  Replicas: 1  Isr: 1
```

**해석:**
- 3개 파티션으로 구성
- 각 파티션은 독립적으로 메시지 저장
- 병렬 처리 가능 (Consumer 3개까지)

## 2. 메시지 샘플링 (개발/디버깅용)

### 어떤 메시지가 들어오는지 확인
```bash
# 최근 10개 메시지만 보기
docker exec kafka kafka-console-consumer --topic user-events --bootstrap-server localhost:9092 --max-messages 10

# 메시지 구조 파악 (키와 함께)
docker exec kafka kafka-console-consumer --topic user-events --bootstrap-server localhost:9092 --from-beginning --max-messages 5 --property print.key=true --property key.separator=" | "
```

### 실시간으로 들어오는 메시지 확인
```bash
# 새로 들어오는 메시지만 실시간 확인
docker exec kafka kafka-console-consumer --topic user-events --bootstrap-server localhost:9092 --property print.timestamp=true
```

## 3. Consumer 상태 모니터링

### 내 Consumer Group 상태 확인
```bash
# Consumer Group 목록
docker exec kafka kafka-consumer-groups --list --bootstrap-server localhost:9092

# 내 Consumer Group 상세 정보
docker exec kafka kafka-consumer-groups --describe --group [내-컨슈머-그룹명] --bootstrap-server localhost:9092
```

### Lag 모니터링 (중요!)
```
GROUP     TOPIC       PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG
my-group  user-events 0          100             105             5
my-group  user-events 1          200             200             0
my-group  user-events 2          150             160             10
```

**LAG 해석:**
- `0`: 실시간 처리 중 (좋음)
- `5-50`: 약간 밀림 (보통)
- `100+`: 많이 밀림 (주의 필요)
- `1000+`: 심각한 지연 (긴급 대응 필요)

## 4. 문제 상황별 대응

### Case 1: Consumer가 메시지를 못 받는 경우
```bash
# 1. 토픽에 메시지가 있는지 확인
docker exec kafka kafka-console-consumer --topic user-events --bootstrap-server localhost:9092 --from-beginning --max-messages 1

# 2. Consumer Group이 제대로 연결됐는지 확인
docker exec kafka kafka-consumer-groups --describe --group [내-그룹명] --bootstrap-server localhost:9092

# 3. 네트워크 연결 확인
telnet [카프카-브로커-주소] 9092
```

### Case 2: Consumer Lag이 계속 증가하는 경우
```bash
# 1. 현재 Lag 상황 파악
docker exec kafka kafka-consumer-groups --describe --group [내-그룹명] --bootstrap-server localhost:9092

# 2. 메시지 유입량 확인 (1분간 들어오는 메시지 수)
timeout 60 docker exec kafka kafka-console-consumer --topic user-events --bootstrap-server localhost:9092 | wc -l

# 3. Consumer 성능 개선 필요 판단
```

### Case 3: 특정 메시지 재처리가 필요한 경우
```bash
# 특정 오프셋부터 다시 처리하도록 설정
docker exec kafka kafka-consumer-groups --reset-offsets --to-offset 100 --group [내-그룹명] --topic user-events --partition 0 --bootstrap-server localhost:9092 --execute
```

## 5. 일상적인 모니터링 스크립트

### 간단한 상태 체크 스크립트
```bash
#!/bin/bash
echo "=== Kafka Consumer 상태 체크 ==="
echo "1. Consumer Group 상태:"
docker exec kafka kafka-consumer-groups --describe --group user-analytics-group --bootstrap-server localhost:9092

echo -e "\n2. 토픽 최신 상태:"
docker exec kafka kafka-run-class kafka.tools.GetOffsetShell --broker-list localhost:9092 --topic user-events

echo -e "\n3. 최근 메시지 샘플:"
docker exec kafka kafka-console-consumer --topic user-events --bootstrap-server localhost:9092 --max-messages 3 --property print.timestamp=true
```

## 6. 회사 환경에서의 팁

### 권한 관련
- 보통 Consumer는 읽기 권한만 있음
- 토픽 생성/삭제는 불가능할 수 있음
- Consumer Group 관리 권한 확인 필요

### 보안 관련
- SASL/SSL 인증이 있을 수 있음
- 네트워크 방화벽 설정 확인
- VPN 연결 필요할 수 있음

### 운영 관련
- Consumer Group 이름은 팀/서비스별로 구분
- 오프셋 리셋은 신중하게 (데이터 중복 처리 위험)
- 로그 레벨 설정으로 디버깅 정보 확보