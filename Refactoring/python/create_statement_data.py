import copy
from functools import reduce
from typing import Dict, Any, List


def create_statement_data(invoice, plays):
    def enrich_performance(perf: Dict) -> Dict:
        result = copy.deepcopy(perf)
        result['play']: Dict = play_for(result)
        result['amount']: int = amount_for(result)
        result['volume_credits']: int = volume_credits_for(result)
        return result

    def play_for(performance):
        return plays[performance['playID']]

    def amount_for(performance: Dict[str, Any]) -> int:
        result: int = 0
        if performance['play']['type'] == 'tragedy':
            result += 40000
            if performance['audience'] > 30:
                result += 1000 * (performance['audience'] - 30)
        elif performance['play']['type'] == 'comedy':
            result += 30000
            if performance['audience'] > 20:
                result += 10000 + 500 * (performance['audience'] - 20)
            result += performance['audience'] * 300
        else:
            raise Exception("Wrong Type!!!")
        return result

    def volume_credits_for(performance: Dict[str, Any]) -> int:
        result = max(performance['audience'] - 30, 0)
        if performance['play']['type'] == 'comedy':
            result += performance['audience'] // 5
        return result

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
