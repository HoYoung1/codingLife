from __future__ import annotations
import dataclasses


@dataclasses.dataclass
class Priority:
    _value: str

    def __init__(self, value: str) -> Union[Priority, None]:
        if isinstance(value, Priority):
            return value
        if value in Priority.legal_values():
            self._value = value
        else:
            raise Exception("invalid value")

    def __str__(self) -> str:
        return self._value

    @classmethod
    def legal_values(cls):
        return ['low', 'normal', 'high', 'rush']

    @property
    def _index(self) -> int:
        return Priority.legal_values().index(self._value)

    def equals(self, other: Priority):
        return self._index == other._index

    def higher_than(self, other: Priority):
        return self._index > other._index

    def lower_than(self, other: Priority):
        return self._index < other._index


from typing import Dict, List, Union


@dataclasses.dataclass
class Order:
    _priority: Priority

    def __init__(self, data: Dict[str, str]) -> None:
        # self._priority: str = data["priority"]
        self._priority: Priority = Priority(data["priority"])

    @property
    def priority(self) -> Priority:
        return self._priority

    # @property
    # def priority_string(self) -> str:
    #     return str(self._priority)

    # @priority_string.setter
    # def priority(self, p: str) -> None:
    #     self._priority = Priority(p)

{
    "":""
}
# client

orders: List[Order] = [
    Order({"priority": "high"}),
    Order({"priority": "rush"}),
    Order({"priority": "low"}),
    Order({"priority": "normal"}),
    Order({"priority": "high"}),
]

print(orders)
# orders[0].priority = "high"
print(orders)
# high_priority_count = len(list(filter(lambda o: o.priority_string == "high" or o.priority_string == "rush", orders)))

# print(high_priority_count)

high_priority_count = len(list(filter(lambda o: o.priority.higher_than(Priority("normal")), orders)))

orders[0].priority.higher_than(Priority("normal"))

