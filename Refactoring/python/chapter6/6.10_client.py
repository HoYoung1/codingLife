reading = {
    "customer": "ivan",
    "quantity": 10,
    "month": 5,
    "year": 2017
}


def acquire_reading():
    return reading


def base_rate(month, year):
    return year * 12 + month


def taxThreshold(year):
    return year


# client 1
aReading = acquire_reading()
baseCharge = base_rate(aReading["month"], aReading["year"]) * aReading["quantity"]

# client 2
aReading = acquire_reading()
base = base_rate(aReading["month"], aReading["year"]) * aReading["quantity"]
taxable_charge = max(0, base - taxThreshold(aReading["year"]))


# client 3
def calculate_base_charge(aReading):
    base_rate(aReading["month"], aReading["year"]) * aReading["quantity"]

aReading = acquire_reading()
basic_charge_amount = calculate_base_charge(aReading)
