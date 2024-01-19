package scanner.ex;

import java.util.Scanner;

public class ScannerEx2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int input = scanner.nextInt();
        if (input % 2 == 0) {
            System.out.println("입력한 " + input + " 은 짝수입니다");
        } else {
            System.out.println("입력한 " + input + " 은 홀수입니다");
        }
    }
}
