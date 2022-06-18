import unittest
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


class TestProvince(unittest.TestCase):
    asia = None

    def setUp(self) -> None:
        self.asia = Province(sample_province_data())

    def test_shortfall(self):
        self.assertEqual(self.asia.get_shortfall(), 5)

    def test_profit(self):
        self.assertEqual(self.asia.get_profit(), 230)

    def test_change_production(self):
        self.asia.producers[0]["production"] = 20
        self.assertEqual(self.asia.get_shortfall(), -6)
        self.assertEqual(self.asia.get_profit(), 292)

    def test_zero_demand(self):
        self.asia.demand = 0
        self.assertEqual(self.asia.get_shortfall(), -25)
        self.assertEqual(self.asia.get_profit(), 0)

    def test_negative_demand(self):
        self.asia.demand = -1
        self.assertEqual(self.asia.get_shortfall(), -26)
        self.assertEqual(self.asia.get_profit(), -10)

    def test_empty_string_demand(self):
        self.asia.demand = ""
        self.assertRaises(TypeError, self.asia.get_shortfall)
        self.assertRaises(TypeError, self.asia.get_profit)


class TestProvinceNoSetup(unittest.TestCase):
    def test_change_production(self):
        data = {
            "name": "Asia",
            "producers": [
                {"name": "Byzantium", "cost": 10, "production": 20},
                {"name": "Attalia", "cost": 12, "production": 10},
                {"name": "Sinope", "cost": 10, "production": 6}
            ],
            "demand": 30,
            "price": 20
        }
        self.asia = Province(data)
        self.assertEqual(self.asia.get_shortfall(), -6)
        self.assertEqual(self.asia.get_profit(), 292)


class TestProvinceNoProducer(unittest.TestCase):
    no_producer = None

    def setUp(self) -> None:
        self.no_producer = Province({
            "name": "No proudcers",
            "producers": [],
            "demand": 30,
            "price": 20
        })

    def test_shortfall(self):
        self.assertEqual(self.no_producer.get_shortfall(), 30)

    def test_profit(self):
        self.assertEqual(self.no_producer.get_profit(), 0)
