package ref.ex;

import java.util.Arrays;

public class ProductOrderMain2 {
    public static void main(String[] args) {
//        ProductOrder productOrder1 = new ProductOrder();
//        productOrder1.productName = "두부";
//        productOrder1.price = 2000;
//        productOrder1.quantity = 2;
//
//        ProductOrder productOrder2 = new ProductOrder();
//        productOrder2.productName = "김치";
//        productOrder2.price = 5000;
//        productOrder2.quantity = 1;
//
//        ProductOrder productOrder3 = new ProductOrder();
//        productOrder3.productName = "콜라";
//        productOrder3.price = 1500;
//        productOrder3.quantity = 2;

        ProductOrder productOrder1 = createOrder("두부", 2000, 2);
        ProductOrder productOrder2 = createOrder("김치", 5000, 1);
        ProductOrder productOrder3 = createOrder("콜라", 1500, 2);

        ProductOrder[] productOrders = {productOrder1, productOrder2, productOrder3};

//        int totalAmount = 0;
//        for (ProductOrder productOrder : productOrders) {
//            System.out.println("상품명 : " + productOrder.productName + " 가격 : " + productOrder.price + " 수량 : " + productOrder.quantity);
//
//            totalAmount += productOrder.price * productOrder.quantity;
//        }
//
//        System.out.println("totalAmount = " + totalAmount);

        printOrders(productOrders);
        System.out.println("total : " + getTotalAmount(productOrders));
    }

    static ProductOrder createOrder(String productName, int price, int quantity) {
        ProductOrder productOrder = new ProductOrder();

        productOrder.productName = productName;
        productOrder.price = price;
        productOrder.quantity = quantity;
        return productOrder;
    }

    static void printOrders(ProductOrder[] productOrders) {
        for (ProductOrder productOrder : productOrders) {
            System.out.println("상품명 : " + productOrder.productName + " 가격 : " + productOrder.price + " 수량 : " + productOrder.quantity);
        }
    }

    static int getTotalAmount(ProductOrder[] productOrders) {
        int result = 0;
        for (ProductOrder productOrder : productOrders) {
            result += productOrder.price * productOrder.quantity;
        }
        return result;
    }

}
