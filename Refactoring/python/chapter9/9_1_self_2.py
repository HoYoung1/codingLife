import dataclasses
from typing import List


@dataclasses.dataclass
class ProductionPlan:
    initial_production: int
    _adjustments: List[int]

    def __init__(self, production) -> None:
        self.initial_production = production
        self._adjustments = []

    @property
    def production(self):
        # return self._production
        return self.initial_production + sum(self._adjustments)

    def applyAdjustment(self, anAdjustment):
        self._adjustments.append(anAdjustment)
