from typing import Dict, Any, List


def voyageRisk(voyage: Dict[str, Any]) -> int:  # 향해 경로 위험요소
    result = 1
    if voyage["length"] > 4:
        result += 2
    if voyage["length"] > 8:
        result += voyage["length"] - 8
    if "중국" in voyage["zone"] and "동인도" in voyage["zone"]:
        result += 4
    return max(result, 0)


def hasChina(history: List[Dict[str, Any]]) -> bool:  # 중국을 경유 하는가?
    return "중국" in map(lambda h: h["zone"], history)


def captainHistoryRisk(voyage: Dict[str, Any], history: List[Dict[str, Any]]) -> int:  # 선장의 향해 이력 위험요소
    result = 1
    if len(history) < 5:
        result += 4
    result += sum([len(h) for h in filter(lambda h: h["profit"], history)])
    if voyage["zone"] == "중국" and hasChina(history):
        result -= 2
    return max(result, 0)


def voyageProfitFactor(voyage: Dict[str, Any], history: List[Dict[str, Any]]) -> int:  # 수익 요인
    result = 2
    if voyage["zone"] == "중국":
        result += 1
    if voyage["zone"] == "동인도":
        result += 1
    if voyage["zone"] == "중국" and hasChina(history):
        result += 3
        if len(history) > 10:
            result += 1
        if voyage["length"] > 12:
            result += 1
        if voyage["length"] > 18:
            result -= 1
    else:
        if len(history) > 8:
            result += 1
        if voyage["length"] > 14:
            result -= 1
    return result


def rating(voyage: Dict[str, Any], history: List[Dict[str, Any]]) -> str:  # 투자 등급
    vpf = voyageProfitFactor(voyage, history)
    vr = voyageRisk(voyage)
    chr = captainHistoryRisk(voyage, history)
    if vpf * 3 > (vr + chr * 2):
        return "A"
    return "B"



### client

_voyage = dict(zone="서인도", length=10)
_history = [
    dict(zone="동인도", profit=5),
    dict(zone="서인도", profit=15),
    dict(zone="중국", profit=-2),
    dict(zone="서아프리카", profit=7),
]

myRating = rating(_voyage, _history)
print(myRating)
assert myRating == "B"
