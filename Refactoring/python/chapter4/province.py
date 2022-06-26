from typing import Dict, Any, List


class Province:
    def __init__(self, doc: Dict[str, Any]):
        self.name: str = doc["name"]
        self.producers: List[Dict] = []
        self.total_production: int = 0
        self.demand: int = doc["demand"]
        self.price: int = doc["price"]

        for producer in doc["producers"]:
            self.add_producer(producer)

    def add_producer(self, arg):
        self.producers.append(arg)
        self.total_production += arg['production']

    # 생산 부족분
    def get_shortfall(self) -> int:
        return self.demand - self.total_production

    # 수익
    def get_profit(self) -> int:
        return self._get_demand_value() - self._get_demand_cost()

    def _get_demand_value(self) -> int:
        return self._get_satified_demand() * self.price

    # min(수요 or 총 생산량) = 30개 요청했지만 25개밖에 못 만들었음.
    def _get_satified_demand(self) -> int:
        return min(self.demand, self.total_production)

    def _get_demand_cost(self) -> int:
        remaining_demand = self.demand
        result = 0
        temp_producers = sorted(self.producers, key=lambda p: p["cost"])
        for producer in temp_producers:
            contribution = min(remaining_demand, producer["production"])
            remaining_demand -= contribution
            result += contribution * producer["cost"]
        return result


class Producer:
    def __init__(self, province: Province, data: Dict[str, Any]):
        self.province = province
        self.cost = data["cost"]
        self.name = data["name"]
        self.production = data["production"] or 0

    def get_name(self) -> str:
        return self.name

    def get_cost(self) -> int:
        return self.cost

    def set_cost(self, arg: str):
        self.cost = int(arg)

    def get_production(self) -> int:
        return self.production

    def set_production(self, amount_str: str):
        amount = int(amount_str)
        new_production = amount if isinstance(amount, int) is amount else 0
        self.province.total_production += new_production - self.production
        self.production = new_production
