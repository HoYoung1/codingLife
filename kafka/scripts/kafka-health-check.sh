#!/bin/bash

# Kafka Consumer 상태 체크 스크립트
# 사용법: ./kafka-health-check.sh [consumer-group-name] [topic-name]

CONSUMER_GROUP=${1:-"user-analytics-group"}
TOPIC=${2:-"user-events"}
BOOTSTRAP_SERVER="localhost:9092"

echo "🔍 Kafka Consumer 상태 체크"
echo "Consumer Group: $CONSUMER_GROUP"
echo "Topic: $TOPIC"
echo "=================================="

# 1. Consumer Group 활성 상태 확인
echo "📊 1. Consumer Group 상태:"
CONSUMER_STATUS=$(docker exec kafka kafka-consumer-groups --describe --group $CONSUMER_GROUP --bootstrap-server $BOOTSTRAP_SERVER 2>/dev/null)

if echo "$CONSUMER_STATUS" | grep -q "No active members"; then
    echo "❌ Consumer Group이 비활성 상태입니다!"
    echo "   - Consumer 애플리케이션이 실행 중인지 확인하세요"
    echo "   - 네트워크 연결 상태를 확인하세요"
else
    echo "✅ Consumer Group이 활성 상태입니다"
    echo "$CONSUMER_STATUS" | grep -E "(CONSUMER-ID|TOPIC|PARTITION|CURRENT-OFFSET|LOG-END-OFFSET|LAG)"
fi

echo ""

# 2. Lag 상태 분석
echo "📈 2. Lag 분석:"
LAG_INFO=$(docker exec kafka kafka-consumer-groups --describe --group $CONSUMER_GROUP --bootstrap-server $BOOTSTRAP_SERVER 2>/dev/null | grep -v "CONSUMER-ID" | grep -v "GROUP")

if [ -n "$LAG_INFO" ]; then
    TOTAL_LAG=0
    MAX_LAG=0
    
    while IFS= read -r line; do
        if [[ $line =~ [0-9]+ ]]; then
            LAG=$(echo $line | awk '{print $NF}')
            if [[ $LAG =~ ^[0-9]+$ ]]; then
                TOTAL_LAG=$((TOTAL_LAG + LAG))
                if [ $LAG -gt $MAX_LAG ]; then
                    MAX_LAG=$LAG
                fi
            fi
        fi
    done <<< "$LAG_INFO"
    
    echo "   총 Lag: $TOTAL_LAG"
    echo "   최대 Lag: $MAX_LAG"
    
    if [ $MAX_LAG -eq 0 ]; then
        echo "   ✅ 실시간 처리 중 (Lag = 0)"
    elif [ $MAX_LAG -lt 100 ]; then
        echo "   ⚠️  약간의 지연 (Lag < 100)"
    elif [ $MAX_LAG -lt 1000 ]; then
        echo "   🚨 지연 발생 (Lag < 1000) - 성능 튜닝 필요"
    else
        echo "   🔥 심각한 지연 (Lag >= 1000) - 긴급 대응 필요"
    fi
else
    echo "   ❌ Lag 정보를 가져올 수 없습니다"
fi

echo ""

# 3. 토픽 상태 확인
echo "📋 3. 토픽 상태:"
TOPIC_INFO=$(docker exec kafka kafka-topics --describe --topic $TOPIC --bootstrap-server $BOOTSTRAP_SERVER 2>/dev/null)

if [ $? -eq 0 ]; then
    echo "✅ 토픽이 존재합니다"
    PARTITION_COUNT=$(echo "$TOPIC_INFO" | grep -c "Partition:")
    echo "   파티션 수: $PARTITION_COUNT"
    
    # 각 파티션의 최신 오프셋 확인
    echo "   파티션별 최신 오프셋:"
    docker exec kafka kafka-run-class kafka.tools.GetOffsetShell --broker-list $BOOTSTRAP_SERVER --topic $TOPIC 2>/dev/null | while read line; do
        echo "     $line"
    done
else
    echo "❌ 토픽을 찾을 수 없습니다"
fi

echo ""

# 4. 최근 메시지 샘플
echo "📨 4. 최근 메시지 샘플 (최대 3개):"
SAMPLE_MESSAGES=$(timeout 5 docker exec kafka kafka-console-consumer --topic $TOPIC --bootstrap-server $BOOTSTRAP_SERVER --max-messages 3 --property print.timestamp=true 2>/dev/null)

if [ -n "$SAMPLE_MESSAGES" ]; then
    echo "$SAMPLE_MESSAGES"
else
    echo "   ⚠️  최근 메시지가 없거나 가져올 수 없습니다"
fi

echo ""
echo "=================================="
echo "✅ 상태 체크 완료"
echo ""
echo "💡 추가 명령어:"
echo "   실시간 모니터링: watch -n 5 './kafka-health-check.sh $CONSUMER_GROUP $TOPIC'"
echo "   Lag 실시간 확인: watch -n 2 'docker exec kafka kafka-consumer-groups --describe --group $CONSUMER_GROUP --bootstrap-server $BOOTSTRAP_SERVER'"