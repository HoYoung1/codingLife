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

# .env 에서 LLM_PROVIDER 읽기
LLM_PROVIDER=$(grep -E '^LLM_PROVIDER=' "$PROJECT_DIR/.env" 2>/dev/null | cut -d'=' -f2 | tr -d '[:space:]')
LLM_PROVIDER="${LLM_PROVIDER:-ollama}"
info "LLM Provider: ${LLM_PROVIDER}"

echo ""
echo -e "${CYAN}========================================${NC}"
echo -e "${CYAN}   Semi-Quality Sentinel  시작${NC}"
echo -e "${CYAN}========================================${NC}"
echo ""

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

# ── Step 1~3: Ollama (ollama 모드일 때만) ─────────────────────
if [ "$LLM_PROVIDER" = "ollama" ]; then

    info "Step 1/6  Ollama 확인..."
    if ! command -v ollama &>/dev/null; then
        warn "Ollama 미설치 — 설치를 시작합니다 (sudo 권한 필요)"
        if ! command -v curl &>/dev/null; then
            error "curl이 없습니다. 'sudo apt-get install curl' 또는 'sudo yum install curl' 로 설치 후 재시도하세요."
        fi
        curl -fsSL https://ollama.com/install.sh | sudo sh
        export PATH="/usr/local/bin:$HOME/.local/bin:$PATH"
    fi
    if ! command -v ollama &>/dev/null; then
        error "Ollama 설치 후에도 명령어를 찾을 수 없습니다. 터미널을 재시작하거나 PATH를 확인하세요."
    fi
    success "Ollama $(ollama --version 2>/dev/null | head -1)"

    info "Step 2/6  Ollama 서버 확인..."
    OLLAMA_RUNNING=false
    if curl -sf http://localhost:11434 &>/dev/null; then
        OLLAMA_RUNNING=true
        info "Ollama 서버 이미 실행 중"
    elif command -v systemctl &>/dev/null && systemctl is-active --quiet ollama 2>/dev/null; then
        OLLAMA_RUNNING=true
        info "Ollama systemd 서비스 실행 중"
    fi
    if [ "$OLLAMA_RUNNING" = false ]; then
        info "Ollama 서버 시작 중..."
        ollama serve > /tmp/ollama.log 2>&1 &
        echo $! >> "$PID_FILE"
        for i in $(seq 1 20); do
            sleep 1
            curl -sf http://localhost:11434 &>/dev/null && break
            if [ "$i" -eq 20 ]; then
                error "Ollama 서버 시작 실패. /tmp/ollama.log 확인하세요."
            fi
        done
    fi
    success "Ollama 서버 http://localhost:11434"

    info "Step 3/6  모델 확인..."
    pull_if_missing() {
        local model="$1"
        if ollama list 2>/dev/null | awk '{print $1}' | grep -qF "${model}"; then
            info "$model 이미 있음"
        else
            warn "$model 다운로드 중... (첫 실행 시 수 GB, 시간이 걸립니다)"
            ollama pull "$model"
        fi
    }
    pull_if_missing "llama3.1:8b"
    pull_if_missing "nomic-embed-text"
    success "모델 준비 완료"

else
    info "Step 1/6  Ollama 건너뜀 (LLM_PROVIDER=azure)"
    info "Step 2/6  Ollama 건너뜀 (LLM_PROVIDER=azure)"
    info "Step 3/6  Ollama 건너뜀 (LLM_PROVIDER=azure)"
fi

# ── Step 4: Python 환경 확인 ──────────────────────────────────
info "Step 4/6  Python 환경 확인..."

# python3 존재 확인
if ! command -v python3 &>/dev/null; then
    error "python3이 없습니다.\n  Ubuntu: sudo apt-get install python3 python3-venv python3-pip\n  CentOS: sudo yum install python3"
fi

# python3-venv 확인 (Ubuntu/Debian 전용)
if python3 -m venv --help &>/dev/null 2>&1; then
    : # venv 사용 가능
else
    warn "python3-venv 없음 — 설치를 시도합니다..."
    if command -v apt-get &>/dev/null; then
        sudo apt-get install -y python3-venv python3-pip
    elif command -v yum &>/dev/null; then
        sudo yum install -y python3-pip
    else
        error "python3-venv 설치에 실패했습니다. 수동으로 설치하세요."
    fi
fi

if [ ! -f "$PYTHON" ]; then
    info ".venv 생성 중..."
    python3 -m venv "$VENV"
fi

info "의존성 설치 중..."
"$VENV/bin/pip" install -q --upgrade pip
"$VENV/bin/pip" install -q -r requirements.txt
success "Python 환경 준비 완료"

# ── Step 5: RAG 인덱싱 ────────────────────────────────────────
info "Step 5/6  FAISS 인덱스 확인..."
if [ ! -f "$PROJECT_DIR/backend/rag/faiss_index/index.faiss" ]; then
    info "인덱스 없음 — RAG 인덱싱 시작..."
    "$PYTHON" -m backend.rag.ingest
else
    info "인덱스 이미 존재"
fi
success "RAG 인덱스 준비 완료"

# ── Step 6: FastAPI + Streamlit 시작 ─────────────────────────
info "Step 6/6  서비스 시작..."

"$VENV/bin/uvicorn" backend.main:app --host 0.0.0.0 --port 8000 \
    > /tmp/fastapi.log 2>&1 &
echo $! >> "$PID_FILE"

for i in $(seq 1 20); do
    sleep 1
    curl -sf http://localhost:8000/health &>/dev/null && break
    if [ "$i" -eq 20 ]; then
        error "FastAPI 시작 실패. 로그 확인: /tmp/fastapi.log"
    fi
done
success "FastAPI  http://localhost:8000"

STREAMLIT_BROWSER_GATHER_USAGE_STATS=false \
"$VENV/bin/streamlit" run frontend/app.py \
    --server.port 8501 \
    --server.headless true \
    > /tmp/streamlit.log 2>&1 &
echo $! >> "$PID_FILE"

for i in $(seq 1 15); do
    sleep 1
    curl -sf http://localhost:8501 &>/dev/null && break
    if [ "$i" -eq 15 ]; then
        error "Streamlit 시작 실패. 로그 확인: /tmp/streamlit.log"
    fi
done
success "Streamlit  http://localhost:8501"

# ── 완료 메시지 ───────────────────────────────────────────────
echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}   모든 서비스 실행 중${NC}"
echo -e "${GREEN}========================================${NC}"
echo -e "  🔬 UI      →  ${CYAN}http://localhost:8501${NC}"
echo -e "  ⚡ API     →  ${CYAN}http://localhost:8000/docs${NC}"
echo -e "  🤖 Ollama  →  ${CYAN}http://localhost:11434${NC}"
echo ""
echo -e "  로그 위치: /tmp/fastapi.log  /tmp/streamlit.log  /tmp/ollama.log"
echo -e "  종료하려면 ${YELLOW}Ctrl+C${NC} 를 누르세요."
echo ""

wait
