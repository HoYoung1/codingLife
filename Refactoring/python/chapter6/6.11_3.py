from typing import Dict


def price_order(product: Dict, quantity: int, shipping_method: Dict):
    base_price = product["basePrice"] * quantity
    discount = max(quantity - product["discountThreshold"], 0) * product["basePrice"] * product["discountRate"]
    price_data = {}  # 중간 데이터
    price = apply_shipping(price_data, base_price, shipping_method, quantity, discount)
    return price


def apply_shipping(price_data, base_price, shipping_method, quantity, discount):
    shipping_per_case = shipping_method["discountedFee"] if base_price > shipping_method["discountThreshold"] else \
        shipping_method["feePerCase"]
    shipping_cost = quantity * shipping_per_case
    price = base_price - discount + shipping_cost
    return price
