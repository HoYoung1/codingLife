package chapter11;

class Order {
    public String deliveryState;
    public PlacedOn placedOn;

    public Order(String deliveryState) {
        this.deliveryState = deliveryState;
        this.placedOn = new PlacedOn();
    }


}
