class AccountType:
    def __init__(self, name_string, interest_rate) -> None:
        self._name = name_string
        self._interest_rate = interest_rate

    @property
    def interest_rate(self):
        return self._interest_rate


class Account:
    def __init__(self, number, type: AccountType):
        self._number = number
        self._type = type

    @property
    def interest_rate(self):
        return self._type.interest_rate






