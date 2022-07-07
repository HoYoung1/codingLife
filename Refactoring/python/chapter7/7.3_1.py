import dataclasses
from typing import Dict, List


@dataclasses.dataclass
class Order:
    _priority: str

    def __init__(self, data: Dict[str, str]) -> None:
        self._priority: str = data["priority"]

    @property
    def priority(self) -> str:
        return self._priority

    @priority.setter
    def priority(self, p: str) -> None:
        self._priority = p


# client
orders: List[Order] = [
    Order({"priority": "high"}),
    Order({"priority": "rush"}),
    Order({"priority": "low"}),
    Order({"priority": "middle"}),
    Order({"priority": "high"}),
]

high_priority_count = len(list(filter(lambda o: o.priority == "high" or o.priority == "rush", orders)))
print(high_priority_count)
