package ref.ex;

import java.util.Scanner;

public class ProductOrderMain3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("입력할 주문의 갯수를 입력하세요 : ");
        int arrayNum = scanner.nextInt();
        scanner.nextLine();

        ProductOrder[] productOrders = new ProductOrder[arrayNum];

        for (int i = 0; i < arrayNum; i++) {
            System.out.println((i+1)+"번째 주문 정보를 입력하세요. ");
            System.out.print("상품명 : ");
            String productName = scanner.nextLine();
            System.out.print("가격 : ");
            int price = scanner.nextInt();
            scanner.nextLine();
            System.out.print("수량 : ");
            int quantity = scanner.nextInt();
            scanner.nextLine();

            productOrders[i] = createOrder(productName, price, quantity);
        }

//        ProductOrder productOrder1 = createOrder("두부", 2000, 2);
//        ProductOrder productOrder2 = createOrder("김치", 5000, 1);
//        ProductOrder productOrder3 = createOrder("콜라", 1500, 2);

//        ProductOrder[] productOrders = {productOrder1, productOrder2, productOrder3};

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
