# Kafka CLI 명령어 가이드

## 기본 명령어 구조

모든 Kafka CLI 명령어는 다음 패턴을 따름:
```bash
kafka-[도구명] --bootstrap-server [브로커주소] [옵션들]
```

Docker 환경에서는:
```bash
docker exec kafka kafka-[도구명] --bootstrap-server localhost:9092 [옵션들]
```

## 1. 토픽 관련 명령어

### 토픽 목록 조회
```bash
docker exec kafka kafka-topics --list --bootstrap-server localhost:9092
```

### 토픽 상세 정보 조회
```bash
# 특정 토픽의 파티션, 리플리케이션 정보
docker exec kafka kafka-topics --describe --topic user-events --bootstrap-server localhost:9092
```

### 토픽 생성
```bash
docker exec kafka kafka-topics --create --topic my-topic --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
```

## 2. 메시지 조회 (Consumer에 영향 없이)

### 토픽의 메시지 읽기 (처음부터)
```bash
docker exec kafka kafka-console-consumer --topic user-events --bootstrap-server localhost:9092 --from-beginning
```

### 최신 메시지만 읽기
```bash
docker exec kafka kafka-console-consumer --topic user-events --bootstrap-server localhost:9092
```

### 특정 파티션의 메시지 읽기
```bash
docker exec kafka kafka-console-consumer --topic user-events --partition 0 --bootstrap-server localhost:9092 --from-beginning
```

### 메시지 키와 함께 보기
```bash
docker exec kafka kafka-console-consumer --topic user-events --bootstrap-server localhost:9092 --from-beginning --property print.key=true --property key.separator=":"
```

**중요**: 이 명령어들은 임시 Consumer Group을 만들어서 읽기만 하므로 기존 Consumer에 영향 없음!

## 3. Consumer Group 관리

### Consumer Group 목록 조회
```bash
docker exec kafka kafka-consumer-groups --list --bootstrap-server localhost:9092
```

### 특정 Consumer Group 상태 조회
```bash
docker exec kafka kafka-consumer-groups --describe --group user-analytics-group --bootstrap-server localhost:9092
```

출력 예시:
```
GROUP           TOPIC       PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG
user-analytics  user-events 0          5               8               3
user-analytics  user-events 1          10              12              2
user-analytics  user-events 2          7               7               0
```

- **CURRENT-OFFSET**: Consumer가 마지막으로 읽은 위치
- **LOG-END-OFFSET**: 토픽의 최신 메시지 위치
- **LAG**: 처리하지 못한 메시지 수 (LOG-END-OFFSET - CURRENT-OFFSET)

### Consumer Group 오프셋 리셋
```bash
# 처음부터 다시 읽도록 설정
docker exec kafka kafka-consumer-groups --reset-offsets --to-earliest --group user-analytics-group --topic user-events --bootstrap-server localhost:9092 --execute
```

## 4. 토픽 오프셋 정보

### 토픽의 최신 오프셋 확인
```bash
docker exec kafka kafka-run-class kafka.tools.GetOffsetShell --broker-list localhost:9092 --topic user-events
```

### 특정 시간대의 오프셋 확인
```bash
# 1시간 전 오프셋
docker exec kafka kafka-run-class kafka.tools.GetOffsetShell --broker-list localhost:9092 --topic user-events --time -3600000
```

## 5. 실시간 모니터링

### Consumer Lag 실시간 모니터링
```bash
watch -n 2 'docker exec kafka kafka-consumer-groups --describe --group user-analytics-group --bootstrap-server localhost:9092'
```

### 토픽에 들어오는 메시지 실시간 확인
```bash
docker exec kafka kafka-console-consumer --topic user-events --bootstrap-server localhost:9092 --property print.timestamp=true
```