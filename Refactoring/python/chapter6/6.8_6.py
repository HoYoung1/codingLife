class NumberRange:
    def __init__(self, min, max) -> None:
        self._data = {"min": min, "max": max}

    def get_min(self):
        return self._data["min"]

    def get_max(self):
        return self._data["max"]


# 정상 범위를 벗어난 측정값을 찾는 함수
def reading_outside_range(station, range):
    return list(filter(lambda r: r["temp"] < range.get_min() or r["temp"] > range.get_max(), station["readings"]))


if __name__ == '__main__':
    station = {
        "name": "ZB1",
        "readings": [
            {"temp": 47, "time": "2016-11-10 09:10"},
            {"temp": 53, "time": "2016-11-10 09:20"},
            {"temp": 58, "time": "2016-11-10 09:30"},
            {"temp": 53, "time": "2016-11-10 09:40"},
            {"temp": 51, "time": "2016-11-10 09:50"}
        ]
    }
    operating_plan = {
        "temperatureFloor": 50,  # 최저 온도
        "temperatureCeiling": 55,  # 최고 온도
    }
    range = NumberRange(operating_plan["temperatureFloor"], operating_plan["temperatureCeiling"])
    alerts = reading_outside_range(
        station,
        range)

    assert alerts == [
        {"temp": 47, "time": "2016-11-10 09:10"},
        {"temp": 58, "time": "2016-11-10 09:30"}
    ]
