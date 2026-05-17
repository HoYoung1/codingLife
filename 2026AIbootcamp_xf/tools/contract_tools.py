import re
from datetime import datetime, timedelta
from pathlib import Path
from langchain_core.tools import tool
from config.settings import CONTRACTS_DIR
from rag.retriever import search_contracts


def _parse_expiry_dates() -> list[dict]:
    results = []
    for txt_file in Path(CONTRACTS_DIR).glob("*.txt"):
        content = txt_file.read_text(encoding="utf-8")
        match = re.search(r"만료일자[:：]\s*(\d{4}-\d{2}-\d{2})", content)
        vendor_match = re.search(r"\[을\]\s*(.+)", content)
        contract_no_match = re.search(r"계약번호[:：]\s*(\S+)", content)
        if match:
            results.append({
                "파일": txt_file.stem,
                "업체명": vendor_match.group(1).strip() if vendor_match else txt_file.stem,
                "계약번호": contract_no_match.group(1) if contract_no_match else "-",
                "만료일": datetime.strptime(match.group(1), "%Y-%m-%d"),
            })
    return results


@tool
def search_contract_conditions(query: str) -> str:
    """계약서에서 특정 조건(금액, SLA, 갱신조건 등)을 RAG로 검색합니다."""
    return search_contracts(query)


@tool
def get_expiring_contracts(days: int = 60) -> str:
    """N일 이내에 만료되는 파트너사 계약 목록을 조회합니다."""
    today = datetime.now()
    cutoff = today + timedelta(days=days)
    contracts = _parse_expiry_dates()

    expiring = [c for c in contracts if today <= c["만료일"] <= cutoff]
    expired = [c for c in contracts if c["만료일"] < today]

    lines = []
    if expired:
        lines.append("🔴 이미 만료된 계약:")
        for c in expired:
            lines.append(f"  - {c['업체명']} ({c['계약번호']}) | 만료: {c['만료일'].strftime('%Y-%m-%d')}")
    if expiring:
        lines.append(f"\n🟡 {days}일 이내 만료 예정:")
        for c in expiring:
            days_left = (c["만료일"] - today).days
            lines.append(
                f"  - {c['업체명']} ({c['계약번호']}) | 만료: {c['만료일'].strftime('%Y-%m-%d')} | 잔여 {days_left}일"
            )

    if not lines:
        return f"{days}일 이내 만료 예정 계약이 없습니다."
    return "\n".join(lines)


@tool
def get_all_contracts_summary() -> str:
    """등록된 모든 파트너사 계약의 요약 현황을 반환합니다."""
    today = datetime.now()
    contracts = _parse_expiry_dates()
    if not contracts:
        return "등록된 계약 정보가 없습니다."

    lines = ["[전체 계약 현황]"]
    for c in sorted(contracts, key=lambda x: x["만료일"]):
        days_left = (c["만료일"] - today).days
        if days_left < 0:
            status = "🔴 만료됨"
        elif days_left <= 30:
            status = f"🟠 {days_left}일 후 만료"
        elif days_left <= 60:
            status = f"🟡 {days_left}일 후 만료"
        else:
            status = f"🟢 {days_left}일 후 만료"
        lines.append(f"  {status} | {c['업체명']} | {c['만료일'].strftime('%Y-%m-%d')}")
    return "\n".join(lines)
