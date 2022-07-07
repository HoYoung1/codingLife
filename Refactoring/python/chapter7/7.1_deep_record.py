customer_data = {
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


def get_raw_customer_data():
    return customer_data


def set_raw_customer_data(arg):
    global customer_data
    customer_data = arg


customerID = 1920
year = 2016
month = 1
amount = 987
get_raw_customer_data()[customerID]["usages"][year][month] = amount


def compare_usage(customerID, laterYear, month):
    later = get_raw_customer_data()[customerID]["usages"][laterYear][month]
    earlier = get_raw_customer_data()[customerID]["usages"][laterYear - 1][month]
    return {"laterAmount": later, "change": later - earlier}


print(compare_usage(customerID, 2016, month))
