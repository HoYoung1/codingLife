import dataclasses
from copy import deepcopy
from typing import Dict, Any, List


@dataclasses.dataclass
class Voyage:
    voyage: Dict[str, Any]
    history: List[Dict[str, Any]]

    def __init__(self,
                 voyage: Dict[str, Any],
                 history: List[Dict[str, Any]]) -> None:
        self.voyage = deepcopy(voyage)
        self.history = deepcopy(history)

    def hasChina(self) -> bool:  # 중국을 경유 하는가?
        return "중국" in map(lambda h: h["zone"], self.history)

    def captainHistoryRisk(self) -> int:  # 선장의 향해 이력 위험요소
        result = 1
        if len(self.history) < 5:
            result += 4
        result += sum([len(h) for h in filter(lambda h: h["profit"] < 0, self.history)])
        return max(result, 0)

    def voyageRisk(self):
        result = 1
        if self.voyage["length"] > 4:
            result += 2
        if self.voyage["length"] > 8:
            result += self.voyage["length"] - 8
        return result


class VoyageChina(Voyage):
    def voyageRisk(self) -> int:  # 향해 경로 위험요소
        result = super().voyageRisk()
        result += 4
        return max(result, 0)

    def captainHistoryRisk(self) -> int:  # 선장의 향해 이력 위험요소
        result = 1
        if len(self.history) < 5:
            result += 4
        result += sum([len(h) for h in filter(lambda h: h["profit"] < 0, self.history)])
        if hasChina(self.history):
            result -= 2
        return max(result, 0)

    def voyageProfitFactor(self) -> int:  # 수익 요인
        result = 3
        if hasChina(self.history):
            result += 3
            if len(self.history) > 10:
                result += 1
            if self.voyage["length"] > 12:
                result += 1
            if self.voyage["length"] > 18:
                result -= 1
        else:
            if len(self.history) > 8:
                result += 1
            if self.voyage["length"] > 14:
                result -= 1
        return result


class VoyageEastIndia(Voyage):
    def voyageRisk(self) -> int:  # 향해 경로 위험요소
        result = super().voyageRisk()
        result += 4
        return max(result, 0)

    def voyageProfitFactor(self) -> int:  # 수익 요인
        return 3


class VoyageWestIndia(Voyage):
    def voyageRisk(self) -> int:  # 향해 경로 위험요소
        result = super().voyageRisk()
        return max(result, 0)

    def voyageProfitFactor(self) -> int:  # 수익 요인
        return 2


class VoyageWestAfrica(Voyage):
    def voyageRisk(self) -> int:  # 향해 경로 위험요소
        result = super().voyageRisk()
        return max(result, 0)

    def voyageProfitFactor(self) -> int:  # 수익 요인
        return 2


def createVoyage(voyage: Dict[str, Any], history: List[Dict[str, Any]]) -> Voyage:
    if voyage["zone"] == "중국":
        return VoyageChina(voyage, history)
    if voyage["zone"] == "동인도":
        return VoyageEastIndia(voyage, history)
    if voyage["zone"] == "서인도":
        return VoyageWestIndia(voyage, history)
    if voyage["zone"] == "서아프리카":
        return VoyageWestAfrica(voyage, history)


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
    result += sum([len(h) for h in filter(lambda h: h["profit"] < 0, history)])
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


### client

def rating(voyage: Dict[str, Any], history: List[Dict[str, Any]]) -> str:  # 투자 등급
    vpf = createVoyage(voyage, history).voyageProfitFactor()
    vr = createVoyage(voyage, history).voyageRisk()
    chr = createVoyage(voyage, history).captainHistoryRisk()
    if vpf * 3 > (vr + chr * 2):
        return "A"
    return "B"


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
