import json

from statement_p25 import statement
from statement_p25_self_refactor import statement_self
from statement_p29 import statement_p29
from statement_p52_self_refactor import statement_p52_self
from python.statement_p59 import statement_p59

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
