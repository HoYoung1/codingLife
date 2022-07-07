import dataclasses

@dataclasses.dataclass
class Priority:
    _value: str

    def __str__(self) -> str:
        return self._value


from typing import Dict, List


@dataclasses.dataclass
class Order:
    _priority: str

    def __init__(self, data: Dict[str, str]) -> None:
        # self._priority: str = data["priority"]
        self._priority: Priority = Priority(data["priority"])

    @property
    def priority_string(self) -> str:
        return str(self._priority)

    @priority_string.setter
    def priority(self, p: str) -> None:
        self._priority = Priority(p)
# client

orders: List[Order] = [
    Order({"priority": "high"}),
    Order({"priority": "rush"}),
    Order({"priority": "low"}),
    Order({"priority": "middle"}),
    Order({"priority": "high"}),
]

print(orders)
orders[0].priority = "kkk"
print(orders)
high_priority_count = len(list(filter(lambda o: o.priority_string == "high" or o.priority_string == "rush", orders)))


print(high_priority_count)

