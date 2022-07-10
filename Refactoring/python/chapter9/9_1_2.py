import dataclasses
from typing import List


@dataclasses.dataclass
class ProductionPlan:
    _production: int
    _adjustments: List[int]

    def __init__(self, production) -> None:
        self._production = production
        self._adjustments = []

    @property
    def production(self):
        return self._production

    def applyAdjustment(self, anAdjustment):
        self._adjustments.append(anAdjustment)
        self._production += anAdjustment.amount
