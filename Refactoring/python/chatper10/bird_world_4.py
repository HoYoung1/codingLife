from __future__ import annotations
import dataclasses
from typing import List, Dict, Union


@dataclasses.dataclass
class Bird:
    bird: Dict[str, Union]


class EuropeanSwallow(Bird):
    @property
    def airSpeedVelocity(self):  # 비행속도
        return 35

    @property
    def plumage(self):  # 깃털 상태
        return "보통이다"


class AfricanSwallow(Bird):
    @property
    def airSpeedVelocity(self):  # 비행속도
        return 40 - 2 * self.bird["numberOfCoconuts"]

    @property
    def plumage(self):  # 깃털 상태
        return "지쳤다" if self.bird["numberOfCoconuts"] > 2 else "보통이다"


class NorwegianBlueParrot(Bird):
    @property
    def airSpeedVelocity(self):  # 비행속도
        return 0 if self.bird["isNailed"] else 10 + self.bird["voltage"] / 10

    @property
    def plumage(self):  # 깃털 상태
        return "그을렸다" if self.bird["voltage"] > 2 else "예쁘다"


def plumages(birds: List[Dict[str, Union]]):
    return {b["name"]: createBird(b).plumage for b in birds}


def speeds(birds: List[Dict[str, Union]]):
    return {b["name"]: createBird(b).airSpeedVelocity for b in birds}


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
assert speeds(test_birds) == {'hy': 35, 'hy2': 32, 'hy3': 19.9}
