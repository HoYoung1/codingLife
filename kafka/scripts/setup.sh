#!/bin/bash

echo "🚀 Kafka 학습 환경 설정 시작..."

# Python 가상환경 생성
echo "📦 Python 가상환경 생성..."
python3 -m venv venv
source venv/bin/activate

# 패키지 설치
echo "📚 Python 패키지 설치..."
pip install -r requirements.txt

# Docker 컨테이너 시작
echo "🐳 Docker 컨테이너 시작..."
docker-compose up -d

# Kafka가 준비될 때까지 대기
echo "⏳ Kafka 서비스 준비 대기..."
sleep 30

# 토픽 생성
echo "📝 기본 토픽 생성..."
docker exec kafka kafka-topics --create --topic user-events --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1

echo "✅ 설정 완료!"
echo ""
echo "🎯 다음 단계:"
echo "1. Kafka UI 확인: http://localhost:8080"
echo "2. Producer 실행: python examples/01_basic_producer.py"
echo "3. Consumer 실행: python examples/02_basic_consumer.py"