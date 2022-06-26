reading = {
    "customer": "ivan",
    "quantity": 10,
    "month": 5,
    "year": 2017
}


class Reading:
    def __init__(self, data) -> None:
        self._customer = data["customer"]
        self._quantity = data["quantity"]
        self._month = data["month"]
        self._year = data["year"]

    def customer(self):
        return self._customer

    def quantity(self):
        return self._quantity

    def month(self):
        return self._month

    def year(self):
        return self._year

    def calculate_base_charge(self):
        return base_rate(self._month, self._year) * self._quantity


def acquire_reading():
    return reading


def base_rate(month, year):
    return year * 12 + month


def taxThreshold(year):
    return year


# client 1
rawReading = acquire_reading()
aReading = Reading(rawReading)
baseCharge = aReading.calculate_base_charge()

# client 2
rawReading = acquire_reading()
aReading = Reading(rawReading)
taxable_charge = max(0, aReading.calculate_base_charge() - taxThreshold(aReading.year()))

# client 3
raw_reading = acquire_reading()
aReading = Reading(raw_reading)
basic_charge_amount = aReading.calculate_base_charge()


print(basic_charge_amount)
