package scanner.ex;

import java.util.Scanner;

public class ScannerEx4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("구구단 단수를 입력하세요");
        int input = scanner.nextInt();

        for (int i = 1; i <= 9; i++) {
            System.out.println(input + " x " + i + " = " + input * i);
        }
    }
}
