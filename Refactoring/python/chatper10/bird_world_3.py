from __future__ import annotations
import dataclasses
from typing import List, Dict, Union



@dataclasses.dataclass
class Bird:
    bird: Dict[str, Union]

    @property
    def plumage(self):  # 깃털 상태
        if self.bird["type"] == "유럽 제비":
            return "보통이다"
        elif self.bird["type"] == "아프리카 제비":
            return "지쳤다" if self.bird["numberOfCoconuts"] > 2 else "보통이다"
        elif self.bird["type"] == "노르웨이 파랑 앵무":
            return "그을렸다" if self.bird["voltage"] > 2 else "예쁘다"
        else:
            return "알 수 없다."

    @property
    def airSpeedVelocity(self):  # 비행속도
        if self.bird["type"] == "유럽 제비":
            return 35
        elif self.bird["type"] == "아프리카 제비":
            return 40 - 2 * self.bird["numberOfCoconuts"]
        elif self.bird["type"] == "노르웨이 파랑 앵무":
            return 0 if self.bird["isNailed"] else 10 + self.bird["voltage"] / 10
        else:
            return None


class EuropeanSwallow(Bird):
    pass


class AfricanSwallow(Bird):
    pass


class NorwegianBlueParrot(Bird):
    pass

##
def plumage(bird: Dict[str, Union]):  # 깃털 상태
    return createBird(bird).plumage


def airSpeedVelocity(bird: Dict[str, Union]):  # 비행속도
    return createBird(bird).airSpeedVelocity


def plumages(birds: List[Dict[str, Union]]):
    return {b["name"]: plumage(b) for b in birds}


def speeds(birds: List[Dict[str, Union]]):
    return {b["name"]: airSpeedVelocity(b) for b in birds}


def createBird(bird: Dict[str, Union]) -> Bird:
    if bird["type"] == "유럽 제비":
        return EuropeanSwallow(bird)
    elif bird["type"] == "아프리카 제비":
        return AfricanSwallow(bird)
    elif bird["type"] == "노르웨이 파랑 앵무":
        return NorwegianBlueParrot(bird)
    else:
        return Bird(bird)


# TEST
test_birds = [
    dict(name="hy", type="유럽 제비", numberOfCoconuts=3, voltage=100, isNailed=True),
    dict(name="hy2", type="아프리카 제비", numberOfCoconuts=4, voltage=101, isNailed=False),
    dict(name="hy3", type="노르웨이 파랑 앵무", numberOfCoconuts=2, voltage=99, isNailed=False),
]

assert plumages(test_birds) == {'hy': '보통이다', 'hy2': '지쳤다', 'hy3': '그을렸다'}
assert speeds(test_birds) == {'hy': 35, 'hy2': 32, 'h3': 19.9}
