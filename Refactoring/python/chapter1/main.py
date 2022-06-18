import json

from python.chapter1.create_statement_data import create_statement_data
from python.chapter1.create_statement_data_p66 import create_statement_data_p66
from python.chapter1.create_statement_data_p73 import create_statement_data_p73
from statement_p25 import statement
from statement_p25_self_refactor import statement_self
from statement_p29 import statement_p29
from statement_p52_self_refactor import statement_p52_self
from python.chapter1.statement_p59 import statement_p59

if __name__ == '__main__':
    invoice: str = ""
    plays: str = ""
    with open('invoices.json', 'r') as f:
        invoice = json.load(f)
    with open('plays.json', 'r') as f:
        plays = json.load(f)

    print(statement(invoice, plays))
    assert statement(invoice, plays) == statement_self(invoice, plays)
    assert statement(invoice, plays) == statement_p29(invoice, plays)
    assert statement(invoice, plays) == statement_p52_self(invoice, plays)
    assert statement(invoice, plays) == statement_p59(invoice, plays)
    assert create_statement_data(invoice, plays) == {'customer': 'BigCo', 'performances': [
        {'playID': 'hamlet', 'audience': 55, 'play': {'name': 'Hamlet', 'type': 'tragedy'}, 'amount': 65000,
         'volume_credits': 25},
        {'playID': 'as-like', 'audience': 35, 'play': {'name': 'As You Like It', 'type': 'comedy'}, 'amount': 58000,
         'volume_credits': 12},
        {'playID': 'othello', 'audience': 40, 'play': {'name': 'Othello', 'type': 'tragedy'}, 'amount': 50000,
         'volume_credits': 10}], 'total_amount': 173000, 'total_volume_credits': 47}
    assert create_statement_data(invoice, plays) == create_statement_data_p66(invoice, plays)
    assert create_statement_data(invoice, plays) == create_statement_data_p73(invoice, plays)
