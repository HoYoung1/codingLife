package scanner;

import java.util.Scanner;

public class ScannerWhile3 {
    public static void main(String[] args) {
        System.out.println("0을 입력하면 프로그램을 종료합니다");

        Scanner scanner = new Scanner(System.in);
        int sum = 0;
        while (true) {
            System.out.println("숫자를 입력하세요");
            int inputNum = scanner.nextInt();

            if (inputNum == 0) {
                System.out.println("현재까지의 합 : " + sum);
                System.out.println("프로그램을 종료합니다");
                break;
            }
            sum += inputNum;
        }
    }
}
