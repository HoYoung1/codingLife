from typing import Dict, Union, List, Any


def statement_p29(invoice: Dict[str, Union[str, List]], plays: Dict[str, Dict]) -> str:
    def play_for(performance):
        return plays[performance['playID']]

    def amount_for(performance: Dict[str, Any]) -> int:
        result: int = 0
        if play_for(performance)['type'] == 'tragedy':
            result += 40000
            if performance['audience'] > 30:
                result += 1000 * (performance['audience'] - 30)
        elif play_for(performance)['type'] == 'comedy':
            result += 30000
            if performance['audience'] > 20:
                result += 10000 + 500 * (performance['audience'] - 20)
            result += performance['audience'] * 300
        else:
            raise Exception("Wrong Type!!!")
        return result

    def usd(number: float):
        return f"{number/100:.2f}"

    def volume_credits_for(performance: Dict[str, Any]):
        result = max(performance['audience'] - 30, 0)
        if play_for(performance)['type'] == 'comedy':
            result += performance['audience'] // 5
        return result

    def total_volume_credits():
        result: int = 0
        for perf in invoice['performances']:
            result += volume_credits_for(perf)
        return result

    def total_amount():
        result: int = 0
        for perf in invoice['performances']:
            result += amount_for(perf)
        return result

    result: str = f"청구 내역 (고객명: {invoice['customer']})\n"
    for perf in invoice['performances']:
        result += f"    {play_for(perf)['name']} : ${usd(amount_for(perf))} ({perf['audience']}석)\n"
    result += f"총액 : ${usd(total_amount())}\n"
    result += f"적립 포인트 : {total_volume_credits()}점\n"
    return result


