package poly.ex.pay1;

import java.util.Scanner;

public class PayMain2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);


        while (true) {

            System.out.print("결제 수단을 입력하세요 : ");
            String paymentMethod = scanner.next();
            if ("exit".equals(paymentMethod) ){
                System.out.println("프로그램을 종료합니다.");
                break;
            }

            System.out.print("결제 금액을 입력하세요 : ");
            int amount = scanner.nextInt();
            scanner.nextLine();

            PayService payService = new PayService();
            payService.processPay(paymentMethod, amount);
        }

//        // kakao 결제
//        String payOption1 = "kakao";
//        int amount1 = 5000;
//        payService.processPay(payOption1, amount1);
//
//        // naver 결제
//        String payOption2 = "naver";
//        int amount2 = 10000;
//        payService.processPay(payOption2, amount2);
//
//
//        // 잘못된 결제 수단 선택
//        String payOption3 = "bad";
//        int amount3 = 15000;
//        payService.processPay(payOption3, amount3);
//
//        // 잘못된 결제 수단 선택
//        String payOption4 = "new";
//        int amount4 = 10000;
//        payService.processPay(payOption4, amount4);
    }
}

