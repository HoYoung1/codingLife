from datetime import datetime


class CustomerContract:
    def __init__(self, start_date) -> None:
        self._start_date = start_date
        self._discount_rate = discount_rate

    @property
    def discount_rate(self):
        return self._discount_rate

    @discount_rate.setter
    def discount_rate(self, n):
        self._discount_rate = n


def date_today():
    return datetime


class Customer:
    def __init__(self, name, discount_rate) -> None:
        self._name = name
        self._contract = CustomerContract(date_today())
        self._set_discount_rate(discount_rate)

    @property
    def discount_rate(self):
        return self.contract.discount_rate

    def _set_discount_rate(self, dr):
        self._contract.discount_rate = dr

    def become_preferred(self):
        # self._discount_rate += 0.03
        # self._set_discount_rate(self.discount_rate + 0.03)
        self.contract.discount_rate = self.discount_rate + 0.03

    def apply_discount(self, amount):
        return amount.subtract(amount.multiply(self.contract.discount_rate))
