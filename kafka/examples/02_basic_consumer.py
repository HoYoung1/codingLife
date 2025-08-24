"""
기초 Kafka Consumer 예제
AWS Kinesis get_records()와 비슷한 개념
"""
import json
from kafka import KafkaConsumer

def create_consumer(topic, group_id):
    """Kafka Consumer 생성"""
    return KafkaConsumer(
        topic,
        bootstrap_servers=['localhost:9092'],
        group_id=group_id,
        # 메시지를 JSON으로 역직렬화
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        key_deserializer=lambda k: k.decode('utf-8') if k else None,
        # 처음부터 읽기 (earliest) vs 최신부터 읽기 (latest)
        auto_offset_reset='earliest',
        # 자동으로 오프셋 커밋
        enable_auto_commit=True,
        auto_commit_interval_ms=1000
    )

def consume_user_events():
    """사용자 이벤트 메시지 소비"""
    topic = 'user-events'
    group_id = 'user-analytics-group'
    
    consumer = create_consumer(topic, group_id)
    
    print(f"📥 {topic} 토픽에서 메시지 수신 시작... (Consumer Group: {group_id})")
    print("메시지를 기다리는 중... (Ctrl+C로 종료)")
    
    try:
        for message in consumer:
            # 메시지 정보 출력
            print(f"\n📨 새 메시지 수신:")
            print(f"   키: {message.key}")
            print(f"   파티션: {message.partition}")
            print(f"   오프셋: {message.offset}")
            print(f"   타임스탬프: {message.timestamp}")
            print(f"   내용: {message.value}")
            
            # 실제 비즈니스 로직 처리
            process_user_event(message.value)
            
    except KeyboardInterrupt:
        print("\n🛑 Consumer 종료 중...")
    finally:
        consumer.close()
        print("✅ Consumer 종료 완료")

def process_user_event(event):
    """사용자 이벤트 처리 로직"""
    action = event.get('action')
    user_id = event.get('user_id')
    
    if action == 'login':
        print(f"   🔐 {user_id} 사용자 로그인 처리")
    elif action == 'view_product':
        product_id = event.get('product_id')
        print(f"   👀 {user_id} 사용자가 {product_id} 상품 조회")
    elif action == 'add_to_cart':
        product_id = event.get('product_id')
        print(f"   🛒 {user_id} 사용자가 {product_id} 상품을 장바구니에 추가")
    elif action == 'purchase':
        order_id = event.get('order_id')
        print(f"   💳 {user_id} 사용자가 {order_id} 주문 완료")

if __name__ == "__main__":
    consume_user_events()