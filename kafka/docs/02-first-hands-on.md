# 첫 번째 실습: Producer와 Consumer

## 실습 목표
- Kafka 클러스터 구축
- Python으로 메시지 생산/소비
- Topic, Partition, Offset 개념 체험

## 1단계: 환경 구축

```bash
# 설정 스크립트 실행
./scripts/setup.sh
```

또는 수동으로:

```bash
# 1. Python 가상환경
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 2. Kafka 클러스터 시작
docker-compose up -d

# 3. 토픽 생성
docker exec kafka kafka-topics --create --topic user-events --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
```

## 2단계: Kafka UI 확인

브라우저에서 http://localhost:8080 접속
- Topics 탭에서 `user-events` 토픽 확인
- 3개의 파티션이 생성된 것을 확인

## 3단계: Producer 실행

```bash
python examples/01_basic_producer.py
```

**예상 출력:**
```
📤 user-events 토픽으로 메시지 전송 시작...
✅ 전송 성공: login | 파티션: 1 | 오프셋: 0
✅ 전송 성공: view_product | 파티션: 2 | 오프셋: 0
✅ 전송 성공: add_to_cart | 파티션: 1 | 오프셋: 1
✅ 전송 성공: purchase | 파티션: 0 | 오프셋: 0
🎉 모든 메시지 전송 완료!
```

## 4단계: Consumer 실행

새 터미널에서:

```bash
source venv/bin/activate
python examples/02_basic_consumer.py
```

**예상 출력:**
```
📥 user-events 토픽에서 메시지 수신 시작...
📨 새 메시지 수신:
   키: user_001
   파티션: 1
   오프셋: 0
   내용: {'user_id': 'user_001', 'action': 'login', ...}
   🔐 user_001 사용자 로그인 처리
```

## 5단계: 관찰 포인트

### 파티셔닝 확인
- 같은 `user_id`를 키로 하는 메시지들이 같은 파티션에 들어가는지 확인
- Kafka UI에서 각 파티션별 메시지 분포 확인

### Consumer Group 동작
- 같은 Consumer Group으로 여러 Consumer 실행해보기
- 파티션별로 Consumer가 분배되는 것 확인

### 오프셋 관리
- Consumer를 중단했다가 다시 시작해보기
- 이미 처리한 메시지는 다시 읽지 않는 것 확인

## 다음 단계 예고

다음에는 더 실전적인 시나리오를 다뤄보자:
- 메시지 직렬화 (Avro, Protobuf)
- 에러 처리와 재시도
- 배치 처리
- 실시간 스트림 처리