import dataclasses
from typing import List


@dataclasses.dataclass
class Bird:
    name: str
    type: str
    numberOfCoconuts: int
    voltage: int
    isNailed: bool


def plumage(bird: Bird):  # 깃털 상태
    if bird.type == "유럽 제비":
        return "보통이다"
    elif bird.type == "아프리카 제비":
        return "지쳤다" if bird.numberOfCoconuts > 2 else "보통이다"
    elif bird.type == "노르웨이 파랑 앵무":
        return "그을렸다" if bird.voltage > 2 else "예쁘다"
    else:
        return "알 수 없다."


def airSpeedVelocity(bird: Bird):  # 비행속도
    if bird.type == "유럽 제비":
        return 35
    elif bird.type == "아프리카 제비":
        return 40 - 2 * bird.numberOfCoconuts
    elif bird.type == "노르웨이 파랑 앵무":
        return 0 if bird.isNailed else 10 + bird.voltage / 10
    else:
        return None


def plumages(birds: List[Bird]):
    return {b.name: plumage(b) for b in birds}


def sppeds(birds: List[Bird]):
    return {b.name: airSpeedVelocity(b) for b in birds}
