# 실무 시나리오별 Kafka 대응법

## 시나리오 1: "Consumer가 메시지를 못 받고 있어요"

### 1단계: 기본 상태 확인
```bash
# Consumer Group이 살아있는지 확인
docker exec kafka kafka-consumer-groups --describe --group [내-그룹명] --bootstrap-server localhost:9092
```

**정상 상태:**
```
CONSUMER-ID                     HOST            CLIENT-ID       #PARTITIONS
consumer-1-abc123              /172.17.0.1     consumer-1      2
consumer-2-def456              /172.17.0.1     consumer-2      1
```

**문제 상태:**
```
No active members.
```

### 2단계: 토픽에 메시지가 있는지 확인
```bash
# 최신 메시지 1개만 확인 (Consumer에 영향 없음)
docker exec kafka kafka-console-consumer --topic user-events --bootstrap-server localhost:9092 --max-messages 1
```

### 3단계: 네트워크 연결 확인
```bash
# Kafka 브로커 연결 테스트
telnet localhost 9092
```

## 시나리오 2: "Consumer Lag이 계속 증가해요"

### 1단계: Lag 상황 파악
```bash
# 실시간 Lag 모니터링
watch -n 5 'docker exec kafka kafka-consumer-groups --describe --group [내-그룹명] --bootstrap-server localhost:9092'
```

### 2단계: 메시지 유입량 측정
```bash
# 1분간 들어오는 메시지 수 측정
timeout 60 docker exec kafka kafka-console-consumer --topic user-events --bootstrap-server localhost:9092 | wc -l
```

### 3단계: 대응 방안
- **Lag < 100**: 정상 범위
- **Lag 100-1000**: Consumer 성능 튜닝 필요
- **Lag > 1000**: Consumer 인스턴스 추가 또는 파티션 증가 검토

## 시나리오 3: "특정 메시지부터 다시 처리하고 싶어요"

### 주의사항
⚠️ **운영 환경에서는 매우 신중하게!** 
- 메시지 중복 처리 발생 가능
- 다른 Consumer 인스턴스 모두 중지 후 실행

### 오프셋 리셋 방법들
```bash
# 1. 처음부터 다시 처리
docker exec kafka kafka-consumer-groups --reset-offsets --to-earliest --group [내-그룹명] --topic user-events --bootstrap-server localhost:9092 --execute

# 2. 특정 오프셋부터 처리
docker exec kafka kafka-consumer-groups --reset-offsets --to-offset 100 --group [내-그룹명] --topic user-events --partition 0 --bootstrap-server localhost:9092 --execute

# 3. 특정 시간부터 처리 (1시간 전)
docker exec kafka kafka-consumer-groups --reset-offsets --to-datetime 2024-01-01T10:00:00.000 --group [내-그룹명] --topic user-events --bootstrap-server localhost:9092 --execute
```

## 시나리오 4: "메시지 형식이 바뀌었는데 어떻게 확인하죠?"

### 최신 메시지 샘플링
```bash
# 최근 5개 메시지 구조 확인
docker exec kafka kafka-console-consumer --topic user-events --bootstrap-server localhost:9092 --max-messages 5 --property print.key=true --property print.timestamp=true
```

### 특정 시간대 메시지 확인
```bash
# 특정 시간 이후 메시지만 확인
docker exec kafka kafka-console-consumer --topic user-events --bootstrap-server localhost:9092 --property print.timestamp=true | grep "2024-01-01"
```

## 시나리오 5: "Consumer가 특정 파티션만 처리 안 해요"

### 파티션별 상태 확인
```bash
# 각 파티션별 메시지 수 확인
docker exec kafka kafka-run-class kafka.tools.GetOffsetShell --broker-list localhost:9092 --topic user-events
```

### 특정 파티션 메시지 확인
```bash
# 파티션 0의 메시지만 확인
docker exec kafka kafka-console-consumer --topic user-events --partition 0 --bootstrap-server localhost:9092 --from-beginning --max-messages 3
```

## 일상적인 모니터링 체크리스트

### 매일 확인할 것들
1. **Consumer Lag**: 1000 이하 유지
2. **Consumer Group 활성 상태**: Active members 존재
3. **에러 로그**: Consumer 애플리케이션 로그 확인

### 주간 확인할 것들
1. **토픽 크기 증가 추세**: 디스크 용량 관리
2. **파티션 분산**: 특정 파티션에 메시지 집중되지 않는지
3. **Consumer 성능**: 처리 시간 추세 분석

### 월간 확인할 것들
1. **토픽 retention 정책**: 메시지 보관 기간 적절성
2. **파티션 수**: 트래픽 증가에 따른 확장 필요성
3. **Consumer Group 정리**: 사용하지 않는 그룹 정리