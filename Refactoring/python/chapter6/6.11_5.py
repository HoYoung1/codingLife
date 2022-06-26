from typing import Dict


def price_order(product: Dict, quantity: int, shipping_method: Dict):
    base_price = product["basePrice"] * quantity
    discount = max(quantity - product["discountThreshold"], 0) * product["basePrice"] * product["discountRate"]
    price_data = {"base_price": base_price, "quantity": quantity, "discount": discount}  # 중간 데이터
    price = apply_shipping(price_data, shipping_method)
    return price


def apply_shipping(price_data, shipping_method):
    shipping_per_case = shipping_method["discountedFee"] if price_data["base_price"] > shipping_method["discountThreshold"] else \
        shipping_method["feePerCase"]
    shipping_cost = price_data["quantity"] * shipping_per_case
    price = price_data["base_price"] - price_data["discount"]  + shipping_cost
    return price
