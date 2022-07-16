from __future__ import annotations
import dataclasses
from typing import List, Dict, Union


@dataclasses.dataclass
class Bird:
    name: str
    type: str
    numberOfCoconuts: int
    voltage: int
    isNailed: bool


def plumage(bird: Dict[str, Union]):  # 깃털 상태
    if bird["type"] == "유럽 제비":
        return "보통이다"
    elif bird["type"] == "아프리카 제비":
        return "지쳤다" if bird["numberOfCoconuts"] > 2 else "보통이다"
    elif bird["type"] == "노르웨이 파랑 앵무":
        return "그을렸다" if bird["voltage"] > 2 else "예쁘다"
    else:
        return "알 수 없다."


def airSpeedVelocity(bird: Dict[str, Union]):  # 비행속도
    if bird["type"] == "유럽 제비":
        return 35
    elif bird["type"] == "아프리카 제비":
        return 40 - 2 * bird["numberOfCoconuts"]
    elif bird["type"] == "노르웨이 파랑 앵무":
        return 0 if bird["isNailed"] else 10 + bird["voltage"] / 10
    else:
        return None


def plumages(birds: List[Dict[str, Union]]):
    return {b["name"]: plumage(b) for b in birds}


def speeds(birds: List[Dict[str, Union]]):
    return {b["name"]: airSpeedVelocity(b) for b in birds}


# TEST
test_birds = [
    dict(name="hy", type="유럽 제비", numberOfCoconuts=3, voltage=100, isNailed=True),
    dict(name="hy2", type="아프리카 제비", numberOfCoconuts=4, voltage=101, isNailed=False),
    dict(name="hy3", type="노르웨이 파랑 앵무", numberOfCoconuts=2, voltage=99, isNailed=False),
]

assert plumages(test_birds) == {'hy': '보통이다', 'hy2': '지쳤다', 'hy3': '그을렸다'}
assert speeds(test_birds) == {'hy': 35, 'hy2': 32, 'hy3': 19.9}
