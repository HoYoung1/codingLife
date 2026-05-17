import pandas as pd
from datetime import datetime, timedelta
from langchain_core.tools import tool
from config.settings import CARD_CSV


def _load() -> pd.DataFrame:
    df = pd.read_csv(CARD_CSV)
    df["만료일"] = pd.to_datetime(df["만료일"])
    return df


@tool
def check_expiring_cards(days: int = 30) -> str:
    """N일 이내에 만료되는 출입통제카드 목록을 조회합니다."""
    df = _load()
    today = datetime.now()
    cutoff = today + timedelta(days=days)
    mask = (df["만료일"] >= today) & (df["만료일"] <= cutoff)
    expiring = df[mask].copy()
    expiring["잔여일수"] = (expiring["만료일"] - today).dt.days

    if expiring.empty:
        return f"{days}일 이내 만료 예정 카드가 없습니다."

    rows = []
    for _, r in expiring.iterrows():
        rows.append(
            f"- {r['직원명']} ({r['사번']}) | {r['부서']} | 만료: {r['만료일'].strftime('%Y-%m-%d')} | 잔여 {int(r['잔여일수'])}일 | 갱신현황: {r['갱신현황']}"
        )
    return f"{days}일 이내 만료 예정 카드 총 {len(expiring)}명:\n" + "\n".join(rows)


@tool
def get_employee_card(employee_id: str) -> str:
    """특정 직원의 출입통제카드 상태를 조회합니다. employee_id는 사번(예: ENG001)입니다."""
    df = _load()
    today = datetime.now()
    row = df[df["사번"] == employee_id.upper()]
    if row.empty:
        return f"사번 {employee_id}에 해당하는 직원을 찾을 수 없습니다."
    r = row.iloc[0]
    days_left = (r["만료일"] - today).days
    status = "만료됨" if days_left < 0 else f"{days_left}일 후 만료"
    return (
        f"직원명: {r['직원명']} ({r['사번']})\n"
        f"부서: {r['부서']}\n"
        f"카드 등급: {r['카드등급']} / 접근 구역: {r['접근구역']}\n"
        f"발급일: {r['발급일']} / 만료일: {r['만료일'].strftime('%Y-%m-%d')}\n"
        f"상태: {status}\n"
        f"갱신 현황: {r['갱신현황']}"
    )


@tool
def get_card_summary() -> str:
    """전체 출입통제카드 현황 요약(만료 임박, 만료됨, 정상)을 반환합니다."""
    df = _load()
    today = datetime.now()
    df["잔여일수"] = (df["만료일"] - today).dt.days

    expired = df[df["잔여일수"] < 0]
    critical = df[(df["잔여일수"] >= 0) & (df["잔여일수"] <= 7)]
    warning = df[(df["잔여일수"] > 7) & (df["잔여일수"] <= 30)]
    normal = df[df["잔여일수"] > 30]

    return (
        f"[출입통제카드 전체 현황]\n"
        f"총 {len(df)}명\n"
        f"  🔴 만료됨: {len(expired)}명\n"
        f"  🟠 7일 이내 만료: {len(critical)}명\n"
        f"  🟡 30일 이내 만료: {len(warning)}명\n"
        f"  🟢 정상: {len(normal)}명"
    )


@tool
def generate_renewal_notification(employee_id: str) -> str:
    """특정 직원에게 보낼 카드 갱신 알림 메시지를 생성합니다."""
    df = _load()
    today = datetime.now()
    row = df[df["사번"] == employee_id.upper()]
    if row.empty:
        return f"사번 {employee_id}에 해당하는 직원을 찾을 수 없습니다."
    r = row.iloc[0]
    days_left = (r["만료일"] - today).days
    return (
        f"[출입통제카드 갱신 안내]\n\n"
        f"안녕하세요, {r['직원명']}님.\n\n"
        f"귀하의 출입통제카드({r['카드등급']}등급, {r['접근구역']})가 "
        f"{r['만료일'].strftime('%Y년 %m월 %d일')}({days_left}일 후)에 만료됩니다.\n\n"
        f"갱신을 위해 PMO팀(pmo@company.com)으로 연락해 주시기 바랍니다.\n"
        f"미갱신 시 출입이 제한될 수 있으니 기한 내 처리 부탁드립니다.\n\n"
        f"감사합니다.\nPMO팀 드림"
    )
