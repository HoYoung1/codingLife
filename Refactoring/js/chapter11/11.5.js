class Order {
    get finalPrice() {
        const basePrice = this.qunatity * this.itemPrice;
        return this.discountedPrice(basePrice)
    }

    discountedPrice(basePrice) {
        switch (this.getDiscountLevel(quantity)) {
            case 1: return basePrice * 0.95;
            case 2: return basePrice * 0.9;
        }
    }

    getDiscountLevel(qunatity) {
        return quantity > 100 ? 2 : 1
    }
}

