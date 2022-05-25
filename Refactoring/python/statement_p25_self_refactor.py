from abc import ABCMeta
from typing import Dict, Union, List


class Play(metaclass=ABCMeta):
    def calculate_fee(self):
        result: int = self.default_amount
        if self.audience > self.free_audience_limit:
            result += self.surcharge_fee_base \
                      + self.surcharge_fee_per_audience * (self.audience - self.free_audience_limit)
        result += self.fee_per_audience * self.audience
        return result / 100

    def calculate_point(self):
        return max(self.audience - 30, 0)


class TragedyPlay(Play):
    def __init__(self, audience: int):
        self.audience = audience
        self.default_amount: int = 40000
        self.fee_per_audience: int = 0

        self.free_audience_limit: int = 30
        self.surcharge_fee_per_audience: int = 1000
        self.surcharge_fee_base = 0


class ComedyPlay(Play):
    def __init__(self, audience: int):
        self.audience = audience
        self.default_amount: int = 30000
        self.fee_per_audience: int = 300

        self.free_audience_limit: int = 20
        self.surcharge_fee_per_audience: int = 500
        self.surcharge_fee_base = 10000

    def calculate_point(self):
        return super().calculate_point() + self.audience // 5


class PlayFactory:
    def __init__(self, type: str):
        self.type = type

    def create(self) -> Play:
        if self.type == 'tragedy':
            return TragedyPlay
        elif self.type == 'comedy':
            return ComedyPlay
        else:
            raise Exception("Wrong Type!!!")


# 각 공연당 비용과 포인트 적립 내역을 출력하는 프로그램
def statement_self(invoice: Dict[str, Union[str, List]], plays: Dict[str, Dict]) -> str:
    total_amount: int = 0
    total_credit: int = 0
    play_history: list = []

    for perf in invoice['performances']:
        play_id: str = perf['playID']
        play_type: str = plays[play_id]['type']
        audience: int = perf['audience']

        play = PlayFactory(play_type).create()(audience)
        this_amount = play.calculate_fee()
        this_credit = play.calculate_point()

        play_history.append(f"    {plays[play_id]['name']} : ${this_amount:.2f} ({perf['audience']}석)")
        total_amount += this_amount
        total_credit += this_credit
    return render_template(
        invoice['customer'],
        '\n'.join(play_history),
        total_amount,
        total_credit
    )


def render_template(customer_name, all_play_history, total_amount, total_credit):
    return f"""청구 내역 (고객명: {customer_name})
{all_play_history}
총액 : ${total_amount:.2f}
적립 포인트 : {total_credit}점
"""
