import dataclasses


class Item:
    pass


@dataclasses.dataclass
class Order:
    _quantity: int
    _item: Item

    @property
    def price(self):
        return self.basePrice * self.discountFactor

    @property
    def discountFactor(self):
        discountFactor = 0.98
        if self.basePrice > 1000:
            discountFactor -= 0.03
        return discountFactor

    @property
    def basePrice(self):
        return self._quantity * self._item.price
