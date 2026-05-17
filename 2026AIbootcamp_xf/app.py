import streamlit as st
import pandas as pd
from datetime import datetime
from config.settings import CARD_CSV, ATTENDANCE_CSV

st.set_page_config(
    page_title="PMO AI Hub",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
.metric-card {
    background: #f8f9fa;
    border-radius: 10px;
    padding: 16px 20px;
    border-left: 5px solid #4a86e8;
}
.critical { border-left-color: #e53935; }
.warning  { border-left-color: #fb8c00; }
.ok       { border-left-color: #43a047; }
.section-title { font-size: 1.1rem; font-weight: 600; margin-bottom: 8px; }
</style>
""", unsafe_allow_html=True)


# ── Sidebar ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.image("https://img.icons8.com/color/96/organization.png", width=60)
    st.title("PMO AI Hub")
    st.caption("Multi-Agent 업무 자동화 시스템")
    st.divider()
    page = st.radio(
        "메뉴",
        ["📊 대시보드", "💬 AI 어시스턴트", "🔔 알림 센터", "📋 종합 리포트"],
        label_visibility="collapsed",
    )
    st.divider()
    st.caption("Powered by LangGraph + Azure OpenAI")


# ── 헬퍼 함수 ────────────────────────────────────────────────────────────────
@st.cache_data(ttl=60)
def load_cards():
    df = pd.read_csv(CARD_CSV)
    df["만료일"] = pd.to_datetime(df["만료일"])
    today = datetime.now()
    df["잔여일수"] = (df["만료일"] - today).dt.days.astype(int)
    return df

@st.cache_data(ttl=60)
def load_attendance():
    df = pd.read_csv(ATTENDANCE_CSV)
    session_cols = [c for c in df.columns if c.endswith("회차")]
    df["출석횟수"] = df[session_cols].apply(lambda r: (r == "O").sum(), axis=1)
    df["총횟수"] = len(session_cols)
    df["출석률(%)"] = (df["출석횟수"] / df["총횟수"] * 100).round(1)
    return df

def card_status_icon(days: int) -> str:
    if days < 0:    return "🔴"
    if days <= 7:   return "🟠"
    if days <= 30:  return "🟡"
    return "🟢"


# ════════════════════════════════════════════════════════════════════════════
# 📊 대시보드
# ════════════════════════════════════════════════════════════════════════════
if page == "📊 대시보드":
    st.title("📊 PMO 대시보드")
    st.caption(f"기준일: {datetime.now().strftime('%Y년 %m월 %d일')}")
    st.divider()

    cards = load_cards()
    attend = load_attendance()
    today = datetime.now()

    expired   = cards[cards["잔여일수"] < 0]
    critical  = cards[(cards["잔여일수"] >= 0) & (cards["잔여일수"] <= 7)]
    warning   = cards[(cards["잔여일수"] > 7)  & (cards["잔여일수"] <= 30)]

    # 계약 만료 파싱 (간단 버전)
    import re
    from pathlib import Path
    from config.settings import CONTRACTS_DIR
    contract_expiries = []
    for f in Path(CONTRACTS_DIR).glob("*.txt"):
        content = f.read_text(encoding="utf-8")
        m = re.search(r"만료일자[:：]\s*(\d{4}-\d{2}-\d{2})", content)
        v = re.search(r"\[을\]\s*(.+)", content)
        if m:
            contract_expiries.append({
                "업체": v.group(1).strip() if v else f.stem,
                "만료일": datetime.strptime(m.group(1), "%Y-%m-%d"),
            })
    expiring_contracts = [c for c in contract_expiries if 0 <= (c["만료일"] - today).days <= 60]

    avg_attendance = attend["출석률(%)"].mean()

    # ── 핵심 지표 ──
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🟠 7일 내 만료 카드", f"{len(critical)}명", delta=None)
    with col2:
        st.metric("🟡 30일 내 만료 카드", f"{len(warning)}명", delta=None)
    with col3:
        st.metric("📄 60일 내 만료 계약", f"{len(expiring_contracts)}건", delta=None)
    with col4:
        st.metric("📚 평균 교육 출석률", f"{avg_attendance:.1f}%", delta=None)

    st.divider()

    # ── 상세 패널 ──
    left, right = st.columns(2)

    with left:
        st.subheader("출입통제카드 만료 현황")
        display_cards = cards[cards["잔여일수"] <= 30].copy()
        if display_cards.empty:
            st.success("30일 이내 만료 예정 카드가 없습니다.")
        else:
            display_cards = display_cards.sort_values("잔여일수")
            display_cards.insert(0, "상태", display_cards["잔여일수"].apply(card_status_icon))
            st.dataframe(
                display_cards[["상태", "직원명", "부서", "만료일", "잔여일수", "갱신현황"]],
                use_container_width=True,
                hide_index=True,
            )

    with right:
        st.subheader("계약 만료 현황")
        if not contract_expiries:
            st.info("등록된 계약이 없습니다.")
        else:
            rows = []
            for c in sorted(contract_expiries, key=lambda x: x["만료일"]):
                d = (c["만료일"] - today).days
                rows.append({
                    "상태": card_status_icon(d),
                    "업체명": c["업체"],
                    "만료일": c["만료일"].strftime("%Y-%m-%d"),
                    "잔여일수": d,
                })
            st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

    st.divider()
    st.subheader("교육 과정별 출석률")
    for course, group in attend.groupby("과정명"):
        avg = group["출석률(%)"].mean()
        low_count = (group["출석률(%)"] < 70).sum()
        color = "normal" if avg >= 80 else ("off" if avg >= 70 else "inverse")
        c1, c2, c3 = st.columns([3, 1, 1])
        with c1:
            st.write(f"📚 **{course}**")
        with c2:
            st.metric("평균 출석률", f"{avg:.1f}%")
        with c3:
            st.metric("주의 인원(70%↓)", f"{low_count}명")
        rank = group.sort_values("출석률(%)", ascending=False)[["직원명", "출석횟수", "총횟수", "출석률(%)"]].reset_index(drop=True)
        rank.index += 1
        st.dataframe(rank, use_container_width=True)


# ════════════════════════════════════════════════════════════════════════════
# 💬 AI 어시스턴트
# ════════════════════════════════════════════════════════════════════════════
elif page == "💬 AI 어시스턴트":
    st.title("💬 PMO AI 어시스턴트")
    st.caption("출입카드 / 계약 / 교육 / 종합 리포트에 대해 자유롭게 질문하세요.")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    example_queries = [
        "30일 이내 만료되는 출입카드 알려줘",
        "Alpha Solutions 계약 갱신 조건이 어떻게 돼?",
        "비즈니스 영어 과정 출석률 순위 보여줘",
        "Gamma Security 계약 SLA 조건 알려줘",
        "이번 달 만료 카드 중 갱신 대기 중인 사람 알림 문자 만들어줘",
    ]
    with st.expander("💡 예시 질문", expanded=False):
        for q in example_queries:
            if st.button(q, key=q):
                st.session_state.pending_query = q

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    query = st.chat_input("질문을 입력하세요...")
    if not query and "pending_query" in st.session_state:
        query = st.session_state.pop("pending_query")

    if query:
        st.session_state.chat_history.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(query)

        with st.chat_message("assistant"):
            with st.spinner("AI Agent가 분석 중입니다..."):
                try:
                    from agents.orchestrator import run_pmo_agent
                    response = run_pmo_agent(query, st.session_state.chat_history[:-1])
                except Exception as e:
                    response = f"오류가 발생했습니다: {str(e)}"
            st.markdown(response)
            st.session_state.chat_history.append({"role": "assistant", "content": response})

    if st.session_state.chat_history:
        if st.button("대화 초기화"):
            st.session_state.chat_history = []
            st.rerun()


# ════════════════════════════════════════════════════════════════════════════
# 🔔 알림 센터
# ════════════════════════════════════════════════════════════════════════════
elif page == "🔔 알림 센터":
    st.title("🔔 알림 센터")
    st.caption("AI가 자동 감지한 갱신 필요 직원 목록과 발송 예정 알림 메시지입니다.")

    cards = load_cards()
    today = datetime.now()
    alert_targets = cards[(cards["잔여일수"] >= 0) & (cards["잔여일수"] <= 30)].sort_values("잔여일수")

    if alert_targets.empty:
        st.success("현재 알림이 필요한 직원이 없습니다.")
    else:
        st.warning(f"⚠️ 총 {len(alert_targets)}명에게 카드 갱신 알림이 필요합니다.")
        st.divider()

        for _, r in alert_targets.iterrows():
            icon = card_status_icon(r["잔여일수"])
            expander_label = f"{icon} {r['직원명']} ({r['부서']}) — {r['잔여일수']}일 후 만료"
            with st.expander(expander_label):
                msg = (
                    f"[출입통제카드 갱신 안내]\n\n"
                    f"안녕하세요, {r['직원명']}님.\n\n"
                    f"귀하의 출입통제카드({r['카드등급']}등급, {r['접근구역']})가 "
                    f"{r['만료일'].strftime('%Y년 %m월 %d일')}({int(r['잔여일수'])}일 후)에 만료됩니다.\n\n"
                    f"갱신을 위해 PMO팀(pmo@company.com)으로 연락해 주시기 바랍니다.\n"
                    f"미갱신 시 출입이 제한될 수 있으니 기한 내 처리 부탁드립니다.\n\n"
                    f"감사합니다.\nPMO팀 드림"
                )
                st.code(msg, language=None)
                col_a, col_b = st.columns([1, 5])
                with col_a:
                    st.button("📤 발송 (시뮬레이션)", key=f"send_{r['사번']}")
                with col_b:
                    st.caption(f"사번: {r['사번']} | 발급일: {r['발급일']} | 갱신현황: {r['갱신현황']}")


# ════════════════════════════════════════════════════════════════════════════
# 📋 종합 리포트 (A2A Report Agent)
# ════════════════════════════════════════════════════════════════════════════
elif page == "📋 종합 리포트":
    st.title("📋 PMO 종합 현황 리포트")
    st.caption(
        "Report Agent가 Access Card Agent → Contract Agent → Training Agent를 "
        "순차 호출(A2A)하여 종합 리포트를 자동 생성합니다."
    )

    st.info(
        "**A2A 흐름**\n"
        "1. Report Agent → Access Card Agent 호출 (카드 현황 수집)\n"
        "2. Report Agent → Contract Agent 호출 (계약 현황 수집)\n"
        "3. Report Agent → Training Agent 호출 (교육 현황 수집)\n"
        "4. GPT-4o로 종합 분석 리포트 생성"
    )

    if st.button("🚀 리포트 생성 (A2A 실행)", type="primary"):
        with st.spinner("A2A Agent 협업 중... (약 30~60초 소요)"):
            try:
                from agents.report_agent import run_report_agent
                result = run_report_agent()

                tab1, tab2, tab3, tab4 = st.tabs(
                    ["📊 종합 리포트", "🪪 카드 현황", "📄 계약 현황", "📚 교육 현황"]
                )
                with tab1:
                    st.markdown(result["report"])
                with tab2:
                    st.text(result["card"])
                with tab3:
                    st.text(result["contract"])
                with tab4:
                    st.text(result["training"])

            except Exception as e:
                st.error(f"리포트 생성 중 오류: {str(e)}")
