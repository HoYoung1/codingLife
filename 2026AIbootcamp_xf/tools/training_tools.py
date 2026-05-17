import pandas as pd
from langchain_core.tools import tool
from config.settings import ENROLLMENT_CSV, ATTENDANCE_CSV


def _load_enrollment() -> pd.DataFrame:
    return pd.read_csv(ENROLLMENT_CSV)


def _load_attendance() -> pd.DataFrame:
    df = pd.read_csv(ATTENDANCE_CSV)
    session_cols = [c for c in df.columns if c.endswith("회차")]
    df["출석횟수"] = df[session_cols].apply(lambda r: (r == "O").sum(), axis=1)
    df["총횟수"] = len(session_cols)
    df["출석률"] = (df["출석횟수"] / df["총횟수"] * 100).round(1)
    return df


@tool
def get_enrollment_status(course_name: str = "") -> str:
    """과정별 수강 신청 현황을 조회합니다. course_name이 없으면 전체를 조회합니다."""
    df = _load_enrollment()
    if course_name:
        df = df[df["과정명"].str.contains(course_name)]
    if df.empty:
        return f"'{course_name}' 과정에 대한 수강 신청 정보가 없습니다."

    lines = []
    for course, group in df.groupby("과정명"):
        lines.append(f"\n[{course}] 수강 신청 {len(group)}명:")
        for _, r in group.iterrows():
            lines.append(f"  - {r['직원명']} ({r['부서']}) | {r['수강상태']}")
    return "수강 신청 현황:" + "\n".join(lines)


@tool
def get_attendance_ranking(course_name: str) -> str:
    """특정 과정의 수강생 출석률 순위를 반환합니다."""
    df = _load_attendance()
    df = df[df["과정명"].str.contains(course_name)]
    if df.empty:
        return f"'{course_name}' 과정에 대한 출석 정보가 없습니다."

    df_sorted = df.sort_values("출석률", ascending=False).reset_index(drop=True)
    lines = [f"[{course_name}] 출석률 순위:"]
    medals = {0: "🥇", 1: "🥈", 2: "🥉"}
    for i, r in df_sorted.iterrows():
        medal = medals.get(i, f"{i+1}위")
        lines.append(f"  {medal} {r['직원명']} | {r['출석횟수']}/{r['총횟수']}회 | {r['출석률']}%")
    return "\n".join(lines)


@tool
def get_training_summary() -> str:
    """전체 교육 과정의 출석률 요약을 반환합니다."""
    df = _load_attendance()
    lines = ["[전체 교육 출석률 현황]"]
    for course, group in df.groupby("과정명"):
        avg = group["출석률"].mean()
        low = (group["출석률"] < 70).sum()
        lines.append(
            f"\n  📚 {course}\n"
            f"     수강인원: {len(group)}명 | 평균 출석률: {avg:.1f}%\n"
            f"     출석률 70% 미만: {low}명"
        )
    return "\n".join(lines)
