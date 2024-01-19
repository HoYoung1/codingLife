package scanner;

import java.util.Scanner;

public class Scanner1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("문자열을 입력하세요");
        String str = scanner.nextLine();
        System.out.println("str = " + str);

        System.out.println("정수를 입력하세요");
        int i = scanner.nextInt();
        System.out.println("i = " + i);
    }
}
