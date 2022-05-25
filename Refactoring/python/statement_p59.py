from typing import Dict, Union, List

from python.create_statement_data import create_statement_data


def statement_p59(invoice: Dict[str, Union[str, List]], plays: Dict[str, Dict]) -> str:
    return render_plain_text(create_statement_data(invoice, plays))


def render_plain_text(data):
    result: str = f"청구 내역 (고객명: {data['customer']})\n"
    for performance in data['performances']:
        result += f"    {performance['play']['name']} : ${usd(performance['amount'])} ({performance['audience']}석)\n"
    result += f"총액 : ${usd(data['total_amount'])}\n"
    result += f"적립 포인트 : {data['total_volume_credits']}점\n"
    return result


def html_statement(invoice: Dict[str, Union[str, List]], plays: Dict[str, Dict]) -> str:
    return render_html(create_statement_data(invoice, plays))


def usd(number: float):
    return f"{number / 100:.2f}"


def render_html(data):
    result: str = f"<h1>청구 내역 (고객명: {data['customer']})</h1>\n"
    result += f'<table>\n'
    result += "<tr><th>연극</th><th>좌석 수</th><th>금액</th></tr>"
    for performance in data['performances']:
        result += f"    <tr><td>{performance['play']['name']}</td><td>(${performance['audience']}석)</td>\n"
        result += f"<td>${usd(performance['amount'])}</td></tr>\n"
    result += f'</table>\n'
    result += f"<p>총액 : <em>${usd(data['total_amount'])}</em></p>\n"
    result += f"<p>적립 포인트 : <em>{data['total_volume_credits']}</em>점</p>\n"
    return result
