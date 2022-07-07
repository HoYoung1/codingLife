import dataclasses
from typing import Dict
from copy import deepcopy

temp_cusomter_data = {
    1920: {
        "name": "마틴 파울러",
        "id": 1920,
        "usages": {
            2016: {
                1: 50,
                2: 55,
                # 나머지 달 생략
            },
            2015: {
                1: 70,
                2: 63,
                # 나머지 달 생략
            }
        }
    },
    38673: {
        "name": "닐 포드",
        "id": 38673
    }
}


@dataclasses.dataclass
class CustomerData:
    _data: Dict

    def __init__(self, data) -> None:
        self._data = data

    @property
    def data(self):
        return self._data

    def set_usage(self, customer_id, year, month, amount):
        self._data[customer_id]["usages"][year][month] = amount

    def get_raw_data(self):
        return deepcopy(self._data)


# }


customer_data = CustomerData(temp_cusomter_data)


def get_raw_customer_data():
    return customer_data.data


def get_customer_data():
    return customer_data


def set_raw_customer_data(arg):
    global customer_data
    customer_data = CustomerData(arg)


customerID = 1920
year = 2016
month = 1
amount = 987


# def set_usage(customer_id, year, month, amount):
#     get_raw_customer_data()[customer_id]["usages"][year][month] = amount


# set_usage(customerID, year, month, amount)
get_customer_data().set_usage(customerID, year, month, amount)


def compare_usage(customerID, laterYear, month):
    later = get_raw_customer_data()[customerID]["usages"][laterYear][month]
    earlier = get_raw_customer_data()[customerID]["usages"][laterYear - 1][month]
    return {"laterAmount": later, "change": later - earlier}


print(compare_usage(customerID, 2016, month))
