from typing import Dict, Union, List


# 각 공연당 비용과 포인트 적립 내역을 출력하는 프로그램
def statement(invoice: Dict[str, Union[str, List]], plays: Dict[str, Dict]) -> str:
    result: str = ""
    total_amount: int = 0
    volume_credits: int = 0

    result += f"청구 내역 (고객명: {invoice['customer']})\n"

    for perf in invoice['performances']:
        this_mount: int = 0
        play_id: str = perf['playID']
        play_type: str = plays[play_id]['type']
        audience: int = perf['audience']

        # 1. 연극 타입에 따른 비용 계산
        if play_type == 'tragedy':
            this_mount += 40000
            this_mount += max(1000 * (audience - 30), 0)
        elif play_type == 'comedy':
            this_mount += 30000
            this_mount += 10000 + max(500 * (audience - 20), 0)
            this_mount += audience * 300
        else:
            raise Exception("Wrong Type!!!")

        # 2. 포인트 적립 계산
        volume_credits += max(audience - 30, 0)
        if play_type == 'comedy':
            volume_credits += audience // 5

        # 3. 출력 --> 각 공연당 비용과 포인트 적립 내역을 리턴
        result += f"    {plays[play_id]['name']} : ${this_mount / 100} ({perf['audience']}석)\n"
        total_amount += this_mount
    result += f"총액 : ${total_amount/100}\n"
    result += f"적립 포인트 : {volume_credits}점\n"
    return result
