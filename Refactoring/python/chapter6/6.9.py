class Reading:
    def base(self):
        pass

    def taxable_charge(self):
        pass

    def calculate_base_charge(self):
        pass

reading = {
    "customer": "ivan",
    "quantity": "10",
    "month": "5",
    "year": 2017
}

aReading = acquireReading()
baseCharge = baseRate(aReading.month, aReading.year) * aRaeding.qua