import dataclasses
from typing import List


@dataclasses.dataclass
class ProductionPlan:
    _adjustments: List[int]

    @property
    def production(self):
        return sum(self._adjustments)

    def applyAdjustment(self, anAdjustment):
        self._adjustments.append(anAdjustment)
