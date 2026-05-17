import os
import httpx
import streamlit as st

# ─── 페이지 설정 ───────────────────────────────────────────────
st.set_page_config(
    page_title="Semi-Quality Sentinel",
    page_icon="🔬",
    layout="wide",
)

URGENCY_CONFIG = {
    "HALT":    {"color": "#FF4B4B", "icon": "🛑", "label": "즉시 가동 중단"},
    "INSPECT": {"color": "#FFA500", "icon": "⚠️", "label": "긴급 점검 필요"},
    "MONITOR": {"color": "#00C48C", "icon": "✅", "label": "모니터링 유지"},
}

SEVERITY_COLOR = {
    "CRITICAL": "#FF4B4B",
    "HIGH":     "#FFA500",
    "MEDIUM":   "#FFD700",
    "LOW":      "#00C48C",
}

# ─── 사이드바 ──────────────────────────────────────────────────
with st.sidebar:
    st.title("⚙️ 설정")
    api_url = st.text_input("FastAPI 서버 URL", value=os.getenv("API_URL", "http://localhost:8000"))
    st.divider()
    st.markdown("**Semi-Quality Sentinel**")
    st.caption("반도체 공정 품질 전조 증상 분석 AI Agent")
    st.caption("LangGraph A2A Multi-Agent 기반")

# ─── 헤더 ─────────────────────────────────────────────────────
st.title("🔬 Semi-Quality Sentinel")
st.markdown("반도체 장비 로그를 입력하면 **3개의 AI Agent**가 협업하여 품질 이상 전조 증상을 분석합니다.")
st.divider()

# ─── 로그 입력 영역 ────────────────────────────────────────────
col_input, col_guide = st.columns([3, 1])

with col_input:
    current_scenario = st.session_state.get("current_scenario", "")
    if current_scenario:
        st.caption(f"🎲 생성된 시나리오: _{current_scenario}_")

    log_text = st.text_area(
        "📋 장비 로그 입력",
        value=st.session_state.get("current_log", ""),
        height=200,
        placeholder="[YYYY-MM-DD HH:MM] SENSOR_PARTICLE: 0.012 (Status: Normal)\n[YYYY-MM-DD HH:MM] EVENT: PM Completed ...",
    )

with col_guide:
    st.markdown("**로그 형식 안내**")
    st.code("[날짜 시간] EVENT: 내용\n[날짜 시간] SENSOR_XXX: 값 (Status: ...)", language="text")
    if st.button("🎲 예시 로그 생성", use_container_width=True, help="AI가 랜덤 시나리오로 로그를 자동 생성합니다"):
        with st.spinner("로그 생성 중..."):
            try:
                with httpx.Client(timeout=60.0) as client:
                    resp = client.get(f"{api_url}/generate-log")
                    resp.raise_for_status()
                    result = resp.json()
                    st.session_state["generated_log"] = result["log_text"]
                    st.session_state["generated_scenario"] = result["scenario"]
            except Exception as e:
                st.error(f"로그 생성 실패: {e}")
        st.rerun()

if st.session_state.get("generated_log"):
    log_text = st.session_state.pop("generated_log")
    scenario = st.session_state.pop("generated_scenario", "")
    st.session_state["current_log"] = log_text
    st.session_state["current_scenario"] = scenario

analyze_btn = st.button("🚀 분석 시작", type="primary", use_container_width=True)

# ─── 분석 실행 ─────────────────────────────────────────────────
if analyze_btn:
    if not log_text or not log_text.strip():
        st.warning("로그를 입력하거나 예시 로그를 불러오세요.")
        st.stop()

    with st.spinner("🤖 AI Agent 분석 중... (30~90초 소요)"):
        try:
            with httpx.Client(timeout=180.0) as client:
                resp = client.post(
                    f"{api_url}/analyze",
                    json={"log_text": log_text},
                )
                resp.raise_for_status()
                data = resp.json()
        except httpx.ConnectError:
            st.error(f"FastAPI 서버에 연결할 수 없습니다: {api_url}\n`uvicorn backend.main:app --reload` 를 실행하세요.")
            st.stop()
        except httpx.HTTPStatusError as e:
            st.error(f"서버 오류: {e.response.status_code} — {e.response.text}")
            st.stop()

    report = data["report"]
    urgency = report.get("urgency", "MONITOR")
    cfg = URGENCY_CONFIG.get(urgency, URGENCY_CONFIG["MONITOR"])

    # ─── 긴급도 배지 ───────────────────────────────────────────
    st.divider()
    st.markdown(
        f"""<div style="background:{cfg['color']}22; border-left:6px solid {cfg['color']};
        padding:16px 20px; border-radius:8px; margin-bottom:16px;">
        <span style="font-size:1.8rem;">{cfg['icon']}</span>
        <span style="font-size:1.4rem; font-weight:700; color:{cfg['color']}; margin-left:12px;">
        긴급도: {urgency} — {cfg['label']}</span></div>""",
        unsafe_allow_html=True,
    )

    # ─── 신뢰도 ────────────────────────────────────────────────
    confidence = report.get("confidence_score", 0.0)
    col_conf1, col_conf2 = st.columns([1, 3])
    with col_conf1:
        st.metric("분석 신뢰도", f"{confidence:.0%}")
    with col_conf2:
        st.progress(confidence)

    # ─── 탭 구성 ───────────────────────────────────────────────
    tab1, tab2, tab3 = st.tabs(["📄 최종 보고서", "📊 분석 상세", "📚 Expert 의견 + RAG 근거"])

    with tab1:
        st.subheader("요약")
        st.info(report.get("summary", ""))

        st.subheader("근본 원인 가설")
        st.warning(report.get("root_cause_hypothesis", ""))

        st.subheader("권고 조치")
        for i, action in enumerate(report.get("recommended_actions", []), 1):
            st.markdown(f"**{i}.** {action}")

        refs = report.get("referenced_standards", [])
        if refs:
            st.subheader("참조 표준 문서")
            for ref in refs:
                st.markdown(f"- 📎 `{ref}`")

    with tab2:
        st.subheader("Analyzer 추세 요약")
        st.markdown(data.get("trend_summary", ""))

        anomalies = report.get("anomalies", [])
        if anomalies:
            st.subheader("감지된 이상치")
            cols = st.columns(len(anomalies)) if len(anomalies) <= 4 else [st.container()]
            for i, a in enumerate(anomalies):
                col = cols[i] if len(anomalies) <= 4 else cols[0]
                sev = a.get("severity", "LOW")
                color = SEVERITY_COLOR.get(sev, "#888")
                with col:
                    st.markdown(
                        f"""<div style="border:2px solid {color}; border-radius:8px;
                        padding:12px; text-align:center;">
                        <div style="font-size:0.85rem; color:#888;">{a.get('sensor','')}</div>
                        <div style="font-size:1.6rem; font-weight:700; color:{color};">
                        {a.get('current_value', 0):.3f}</div>
                        <div style="font-size:0.8rem;">기준: {a.get('threshold', 0):.3f}</div>
                        <div style="background:{color}; color:white; border-radius:4px;
                        padding:2px 8px; margin-top:6px; font-size:0.8rem;">{sev}</div>
                        </div>""",
                        unsafe_allow_html=True,
                    )
        else:
            st.success("이상치가 감지되지 않았습니다.")

    with tab3:
        st.subheader("Standard Expert 의견")
        st.markdown(data.get("expert_opinion", ""))

        st.subheader("RAG 검색 결과 (참조 매뉴얼 청크)")
        with st.expander("매뉴얼 원문 보기"):
            st.text(data.get("rag_context", ""))
