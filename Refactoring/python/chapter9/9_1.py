import dataclasses
from typing import List


@dataclasses.dataclass
class ProductionPlan:
    _production: int
    _adjustments: List[int]

    @property
    def production(self):
        return self._production

    def applyAdjustment(self, anAdjustment):
        self._adjustments.append(anAdjustment)
        self._production += anAdjustment.amount
