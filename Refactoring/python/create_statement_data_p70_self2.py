import copy
from functools import reduce
from typing import Dict, List


class PerformanceCalculator:

    def __init__(self, performance: Dict, play: Dict) -> None:
        self.performance = performance
        self.play = play
        self.amount = self.get_amount()
        self.volume_credit = self.get_volume_credit()

    def get_amount(self) -> int:
        raise Exception("서브클래스에서 호출되도록 설계되었습니다.")

    def get_volume_credit(self) -> int:
        result = max(self.performance['audience'] - 30, 0)
        return result


class TragedyCalculator(PerformanceCalculator):
    def get_amount(self) -> int:
        result: int = 0
        result += 40000
        if self.performance['audience'] > 30:
            result += 1000 * (self.performance['audience'] - 30)
        return result


class ComedyCalculator(PerformanceCalculator):
    def get_amount(self) -> int:
        result: int = 0
        result += 30000
        if self.performance['audience'] > 20:
            result += 10000 + 500 * (self.performance['audience'] - 20)
        result += self.performance['audience'] * 300
        return result

    def get_volume_credit(self) -> int:
        result = 0
        result += super().volume_credit
        result += self.performance['audience'] // 5
        return result


def create_performance_calculator(performance: Dict, play: Dict) -> PerformanceCalculator:
    if performance['type'] == 'tragedy':
        return TragedyCalculator(performance, play)
    elif performance['type'] == 'comedy':
        return ComedyCalculator(performance, play)
    raise Exception("Wrong Type!!!")


def create_statement_data_p66(invoice, plays):
    def enrich_performance(perf: Dict) -> Dict:
        calculator = create_performance_calculator(perf, play_for(perf))
        result = copy.deepcopy(perf)
        result['play']: Dict = calculator.play
        result['amount']: int = calculator.amount
        result['volume_credits']: int = calculator.volume_credit
        return result

    def play_for(performance):
        return plays[performance['playID']]

    def total_amount(data: Dict) -> int:
        # 1.
        # result: int = 0
        # for performance in data['performances']:
        #     result += performance['amount']

        # 2.
        # result = sum([p['amount'] for p in data['performances']])

        # 3.
        result = reduce(lambda acc, cur: acc + cur['amount'], data['performances'], 0)
        return result

    def total_volume_credits(data: Dict) -> int:
        # 1.
        # result: int = 0
        # for performance in data['performances']:
        #     result += performance['volume_credits']

        # 2.
        result = reduce(lambda acc, cur: acc + cur['volume_credits'], data['performances'], 0)
        return result

    statement_data: Dict = {}
    statement_data['customer']: str = invoice['customer']
    statement_data['performances']: List = list(map(enrich_performance, invoice['performances']))
    statement_data['total_amount']: int = total_amount(statement_data)
    statement_data['total_volume_credits']: int = total_volume_credits(statement_data)
    return statement_data
