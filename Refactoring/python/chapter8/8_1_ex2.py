class Account:
    @property
    def bank_charge(self):
        result = 4.5
        if self._days_overdrawn > 0:
            result += self.overdraft_charge
        return result

    @property
    def overdraft_charge(self):
        if self.type["isPremium"]:
            base_charge = 10
            if self.days_overdrawn <= 7:
                return base_charge
            else:
                return base_charge + (self.days_overdrawn - 7) * 0.85
        else:
            return self.days_overdrawn * 1.75


