package chapter11;

public class Delivery2 {
    public static void main(String[] args) {
        
    }

    public  static int deliveryDate(Order anOrder, Boolean isRush) {
        if (isRush) {
            int result;
            int deliveryTime;

            if (anOrder.deliveryState.equals("MA")  || anOrder.deliveryState.equals("CT"))
                deliveryTime = 1;
            else if (anOrder.deliveryState.equals("NY") || anOrder.deliveryState.equals("NH")) {
                deliveryTime = 2;
            }
            else deliveryTime = 3;
            result =  2 + deliveryTime;
            result = result - 1;
            return result;
        } else {
            int result;
            int deliveryTime;

            if (anOrder.deliveryState.equals("MA")  || anOrder.deliveryState.equals("CT"))
                deliveryTime = 2;
            else if (anOrder.deliveryState.equals("NY") || anOrder.deliveryState.equals("NH")) {
                deliveryTime = 2;
                if(anOrder.deliveryState.equals("NH"))
                    deliveryTime = 3;
            }
            else if (anOrder.deliveryState.equals("ME"))
                deliveryTime = 3;
            else
                deliveryTime = 4;
            result =  2 + deliveryTime;
            return result;
        }
    }

}
