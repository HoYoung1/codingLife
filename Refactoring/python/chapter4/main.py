from typing import Dict, Any

from python.chapter4.province import Province


def sample_province_data() -> Dict[str, Any]:
    return {
        "name": "Asia",
        "producers": [
            {"name": "Byzantium", "cost": 10, "production": 9},
            {"name": "Attalia", "cost": 12, "production": 10},
            {"name": "Sinope", "cost": 10, "production": 6}
        ],
        "demand": 30,
        "price": 20
    }


if __name__ == '__main__':
    asia: Province = Province(sample_province_data())  # 픽스처 설정
    assert asia.get_shortfall() == 5  # 검증
    assert asia.get_profit() == 230
