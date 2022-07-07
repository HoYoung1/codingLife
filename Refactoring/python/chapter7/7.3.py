from typing import Dict, List


class Order:
    def __init__(self, data: Dict[str, str]) -> None:
        self.priority: str = data["priority"]
        # 생략


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
