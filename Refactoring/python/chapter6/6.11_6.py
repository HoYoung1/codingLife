from typing import Dict


def price_order(product: Dict, quantity: int, shipping_method: Dict):
    price_data = calculate_pricing_data(product, quantity)
    return apply_shipping(price_data, shipping_method)


def calculate_pricing_data(product, quantity):
    base_price = product["basePrice"] * quantity
    discount = max(quantity - product["discountThreshold"], 0) * product["basePrice"] * product["discountRate"]
    return {"base_price": base_price, "quantity": quantity, "discount": discount}


def apply_shipping(price_data, shipping_method):
    shipping_per_case = shipping_method["discountedFee"] if price_data["base_price"] > shipping_method["discountThreshold"] else \
        shipping_method["feePerCase"]
    shipping_cost = price_data["quantity"] * shipping_per_case
    return price_data["base_price"] - price_data["discount"] + shipping_cost
