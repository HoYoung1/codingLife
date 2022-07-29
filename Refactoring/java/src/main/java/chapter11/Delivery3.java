package chapter11;

public class Delivery3 {
    public  static int deliveryDate(Order anOrder, Boolean isRush) {
        int result;
        int deliveryTime;

        if (anOrder.deliveryState.equals("MA")  || anOrder.deliveryState.equals("CT"))
            deliveryTime = isRush? 1: 2;
        else if (anOrder.deliveryState.equals("NY") || anOrder.deliveryState.equals("NH")) {
            deliveryTime = 2;
            if(anOrder.deliveryState.equals("NH") && !isRush)
                deliveryTime = 3;
        }
        else if (isRush)
            deliveryTime = 3;
        else if (anOrder.deliveryState.equals("ME"))
            deliveryTime = 3;
        else
            deliveryTime = 4;
        result =  anOrder.placedOn.plusDays(2 + deliveryTime);
        if (isRush) result = result - 1;
        return result;
    }
}
