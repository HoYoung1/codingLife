package scanner.ex;

import java.util.Scanner;

public class ScannerWhileEx2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("상품의 가격을 입력하세요: (-1을 입력하면 종료)");
            int productPrice = scanner.nextInt();

            if (productPrice == -1) {
                break;
            }

            System.out.print("구매하려는 수량을 입력하세요");
            int productQuantity = scanner.nextInt();

            System.out.println("총 비용 : " + productPrice * productQuantity);
        }
    }
}
