from datetime import datetime


class CustomerContract:
    def __init__(self, start_date) -> None:
        self._start_date = start_date


def date_today():
    return datetime


class Customer:
    def __init__(self, name, discount_rate) -> None:
        self._name = name
        self._discount_rate = discount_rate
        self.contract = CustomerContract(date_today())

    @property
    def discount_rate(self):
        return self._discount_rate

    def become_preferred(self):
        self._discount_rate += 0.03

    def apply_discount(self, amount):
        return amount.subtract(amount.multiply(self._discount_rate))
