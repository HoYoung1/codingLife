SHELL := /bin/bash
PROJECT_DIR := $(shell pwd)
LOG_FILE    := $(PROJECT_DIR)/logs/app.log
PID_DIR     := $(PROJECT_DIR)/.pids

.PHONY: start stop start-loki start-alloy start-app start-grafana logs status clean

## ── 전체 시작 ─────────────────────────────────────────────────────────────
start: _mkdir start-loki _wait start-alloy start-app start-grafana
	@echo ""
	@echo "  All services started."
	@echo "  Grafana  → http://localhost:3000  (admin / admin)"
	@echo "  Loki     → http://localhost:3100"
	@echo ""
	@echo "  make logs    — 로그 실시간 확인"
	@echo "  make status  — 프로세스 상태 확인"
	@echo "  make stop    — 전체 종료"

## ── 개별 시작 ─────────────────────────────────────────────────────────────
start-loki: _mkdir
	@echo "[loki] Starting..."
	@loki -config.file=$(PROJECT_DIR)/loki-config.yaml \
	      > $(PROJECT_DIR)/logs/loki.log 2>&1 & \
	echo $$! > $(PID_DIR)/loki.pid
	@echo "[loki] PID=$$(cat $(PID_DIR)/loki.pid)"

start-alloy: _mkdir
	@echo "[alloy] Starting..."
	@alloy run $(PROJECT_DIR)/config.alloy \
	      > $(PROJECT_DIR)/logs/alloy.log 2>&1 & \
	echo $$! > $(PID_DIR)/alloy.pid
	@echo "[alloy] PID=$$(cat $(PID_DIR)/alloy.pid)"

start-app: _mkdir
	@echo "[app] Starting dummy_app.py..."
	@python3 $(PROJECT_DIR)/dummy_app.py \
	      > /dev/null 2>&1 & \
	echo $$! > $(PID_DIR)/app.pid
	@echo "[app] PID=$$(cat $(PID_DIR)/app.pid)"

start-grafana:
	@echo "[grafana] Starting..."
	@brew services start grafana
	@echo "[grafana] http://localhost:3000"

## ── 전체 종료 ─────────────────────────────────────────────────────────────
stop:
	@echo "Stopping services..."
	@for svc in loki alloy app; do \
	  pid_file=$(PID_DIR)/$$svc.pid; \
	  if [ -f $$pid_file ]; then \
	    pid=$$(cat $$pid_file); \
	    kill $$pid 2>/dev/null && echo "[$$svc] Stopped (PID=$$pid)" || echo "[$$svc] Already stopped"; \
	    rm -f $$pid_file; \
	  fi; \
	done
	@brew services stop grafana
	@echo "Done."

## ── 유틸 ──────────────────────────────────────────────────────────────────
logs:
	@tail -f $(LOG_FILE)

status:
	@echo "── Process status ──────────────────────────"
	@for svc in loki alloy app; do \
	  pid_file=$(PID_DIR)/$$svc.pid; \
	  if [ -f $$pid_file ]; then \
	    pid=$$(cat $$pid_file); \
	    if kill -0 $$pid 2>/dev/null; then \
	      echo "  [$$svc] RUNNING (PID=$$pid)"; \
	    else \
	      echo "  [$$svc] DEAD (stale PID=$$pid)"; \
	    fi; \
	  else \
	    echo "  [$$svc] NOT STARTED"; \
	  fi; \
	done
	@brew services info grafana --json 2>/dev/null \
	  | python3 -c "import sys,json; s=json.load(sys.stdin); print(f'  [grafana] {s[\"status\"].upper()}')" 2>/dev/null || true
	@echo "────────────────────────────────────────────"

clean:
	@rm -rf $(PROJECT_DIR)/logs $(PID_DIR) /tmp/loki-data
	@echo "Cleaned logs, pids, and loki data."

## ── 내부 헬퍼 ─────────────────────────────────────────────────────────────
_mkdir:
	@mkdir -p $(PROJECT_DIR)/logs $(PID_DIR)

_wait:
	@sleep 2
