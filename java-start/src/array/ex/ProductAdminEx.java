package array.ex;

import java.util.Scanner;

public class ProductAdminEx {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int maxProducts = 10;

        String[] productNames = new String[maxProducts];
        int[] productPrices = new int[maxProducts];
        int productCount = 0;
        while (true) {
            System.out.println("1. 상품등록 | 2. 상품목록 | 3. 종료");

            System.out.print("메뉴를 선택하세요:");
            int menuNum = scanner.nextInt();
            scanner.nextLine();

            if (menuNum == 1) {
                System.out.print("상품 이름을 입력하세요: ");
                String productName = scanner.nextLine();
                System.out.print("상품 가격을 입력하세요: ");
                int productPrice = scanner.nextInt();
                scanner.nextLine();
                productNames[productCount] = productName;
                productPrices[productCount] = productPrice;
                productCount += 1;
            }

            if (menuNum == 2) {
                if (productCount == 0) {
                    System.out.println("등록된 상품이 없습니다.");
                }
                for (int i = 0; i < productCount; i++) {
                    System.out.println(productNames[productCount] + ": " + productPrices[productCount] + "원 ");
                }
            }

            if (menuNum == 3) {
                System.out.println("프로그램을 종료합니다.");
                break;
            }
        }
    }
}
