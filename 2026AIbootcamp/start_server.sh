#!/bin/bash
set -e

# ── 색상 출력 ───────────────────────────────────────────────────
GREEN='\033[0;32m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; CYAN='\033[0;36m'; NC='\033[0m'
info()    { echo -e "${CYAN}[INFO]${NC} $1"; }
success() { echo -e "${GREEN}[OK]${NC}   $1"; }
warn()    { echo -e "${YELLOW}[WARN]${NC} $1"; }
error()   { echo -e "${RED}[ERR]${NC}  $1"; exit 1; }

# ── 스크립트 위치 기준으로 프로젝트 루트 설정 ─────────────────
PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$PROJECT_DIR"

VENV="$PROJECT_DIR/.venv"
PYTHON="$VENV/bin/python"
PID_FILE="/tmp/semi-sentinel.pids"

echo ""
echo -e "${CYAN}========================================${NC}"
echo -e "${CYAN}   Semi-Quality Sentinel  서버 시작${NC}"
echo -e "${CYAN}========================================${NC}"
echo ""
info "LLM Provider: azure"

# ── 종료 시 백그라운드 프로세스 정리 ──────────────────────────
cleanup() {
    echo ""
    info "서비스 종료 중..."
    if [ -f "$PID_FILE" ]; then
        while read -r pid; do
            kill "$pid" 2>/dev/null && info "PID $pid 종료" || true
        done < "$PID_FILE"
        rm -f "$PID_FILE"
    fi
    success "종료 완료"
}
trap cleanup EXIT INT TERM
> "$PID_FILE"

# HTTP 헬스체크 함수 (curl 없이 Python urllib 사용)
http_check() {
    local url="$1"
    python -c "
import urllib.request, sys
try:
    urllib.request.urlopen('$url', timeout=3)
    sys.exit(0)
except:
    sys.exit(1)
" 2>/dev/null
}

# ── Step 1: Python 환경 확인 ──────────────────────────────────
info "Step 1/3  Python 환경 확인..."

if [ ! -f "$PYTHON" ]; then
    info ".venv 생성 중..."
    python -m venv "$VENV"
fi

info "의존성 설치 중..."
"$VENV/bin/pip" install -q --upgrade pip
"$VENV/bin/pip" install -q -r requirements.txt
success "Python 환경 준비 완료"

# ── Step 2: RAG 인덱싱 ────────────────────────────────────────
info "Step 2/3  FAISS 인덱스 확인..."
if [ ! -f "$PROJECT_DIR/backend/rag/faiss_index/index.faiss" ]; then
    info "인덱스 없음 — RAG 인덱싱 시작..."
    LLM_PROVIDER=azure "$PYTHON" -m backend.rag.ingest
else
    info "인덱스 이미 존재"
fi
success "RAG 인덱스 준비 완료"

# ── Step 3: FastAPI + Streamlit 시작 ─────────────────────────
info "Step 3/3  서비스 시작..."

uvicorn backend.main:app --host 0.0.0.0 --port 8000 \
    > /tmp/fastapi.log 2>&1 &
echo $! >> "$PID_FILE"
info "FastAPI 시작 대기 중..."
success "FastAPI  http://localhost:8000"


# ── 완료 메시지 ───────────────────────────────────────────────
echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}   모든 서비스 실행 중${NC}"
echo -e "${GREEN}========================================${NC}"
echo -e "  API  →  ${CYAN}http://localhost:8000/docs${NC}"
echo ""
echo -e "  로그 위치: /tmp/fastapi.log  
echo -e "  종료하려면 ${YELLOW}Ctrl+C${NC} 를 누르세요."
echo ""

wait