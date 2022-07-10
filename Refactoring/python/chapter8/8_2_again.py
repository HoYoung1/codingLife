from datetime import datetime


class CustomerContract:
    def __init__(self, start_date) -> None:
        self._start_date = start_date
        self._discount_rate = None

    @property
    def discount_rate(self):
        return self._discount_rate

    @discount_rate.setter
    def discount_rate(self, arg):
        self._discount_rate = arg


def date_today():
    return datetime


class Customer:
    def __init__(self, name, discount_rate) -> None:
        self._name = name
        self._contract = CustomerContract(date_today())
        self._set_discount_rate(discount_rate)

    @property
    def discount_rate(self):
        return self._contract.discount_rate

    def _set_discount_rate(self, arg):
        self._contract.discount_rate = arg

    def become_preferred(self):
        self._set_discount_rate(self._discount_rate + 0.03)

    def apply_discount(self, amount):
        return amount.subtract(amount.multiply(self._discount_rate))
