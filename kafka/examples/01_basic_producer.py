"""
기초 Kafka Producer 예제
AWS Kinesis put_record()와 비슷한 개념
"""
import json
import time
from kafka import KafkaProducer
from datetime import datetime

def create_producer():
    """Kafka Producer 생성"""
    return KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        # 메시지를 JSON으로 직렬화
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        key_serializer=lambda k: k.encode('utf-8') if k else None
    )

def send_user_events():
    """사용자 이벤트 메시지 전송"""
    producer = create_producer()
    topic = 'user-events'
    
    # 샘플 이벤트들
    events = [
        {'user_id': 'user_001', 'action': 'login', 'timestamp': datetime.now().isoformat()},
        {'user_id': 'user_002', 'action': 'view_product', 'product_id': 'prod_123', 'timestamp': datetime.now().isoformat()},
        {'user_id': 'user_001', 'action': 'add_to_cart', 'product_id': 'prod_123', 'timestamp': datetime.now().isoformat()},
        {'user_id': 'user_003', 'action': 'purchase', 'order_id': 'order_456', 'timestamp': datetime.now().isoformat()},
    ]
    
    print(f"📤 {topic} 토픽으로 메시지 전송 시작...")
    
    for event in events:
        # user_id를 키로 사용 (같은 사용자의 이벤트는 같은 파티션으로)
        key = event['user_id']
        
        # 메시지 전송 (비동기)
        future = producer.send(topic, key=key, value=event)
        
        # 전송 결과 확인
        try:
            record_metadata = future.get(timeout=10)
            print(f"✅ 전송 성공: {event['action']} | 파티션: {record_metadata.partition} | 오프셋: {record_metadata.offset}")
        except Exception as e:
            print(f"❌ 전송 실패: {e}")
        
        time.sleep(1)  # 1초 간격으로 전송
    
    # 모든 메시지가 전송될 때까지 대기
    producer.flush()
    producer.close()
    print("🎉 모든 메시지 전송 완료!")

if __name__ == "__main__":
    send_user_events()