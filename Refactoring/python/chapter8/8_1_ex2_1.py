class Account:
    def __init__(self, at):
        self.type: AccountType = at

    @property
    def days_overdrawn(self):
        return 3

    @property
    def bank_charge(self):  # 은행 이자 계산
        result = 4.5
        if self.days_overdrawn > 0:
            result += self.overdraft_charge
        return result

    @property
    def overdraft_charge(self):  # 초과 인출 이자 계산
        return self.type.moving_overdraft_charge(3)




class AccountType:
    def __init__(self, t: str) -> None:
        self._type: str = t

    @property
    def moving_overdraft_charge(self, days_overdrawn: int):  # 초과 인출 이자 계산
        if self.type == "isPremium":
            base_charge = 10
            if days_overdrawn <= 7:
                return base_charge
            else:
                return base_charge + (days_overdrawn - 7) * 0.85
        else:
            return days_overdrawn * 1.75
