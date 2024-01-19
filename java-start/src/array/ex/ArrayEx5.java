package array.ex;

import java.util.Scanner;

public class ArrayEx5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("입력 받을 숫자의 갯수를 입력하세요");
        int inputNum = scanner.nextInt();
        int[] numbers = new int[inputNum];

        System.out.println("정수를 입력하세요");
        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = scanner.nextInt();
        }

//        System.out.println("출력");
//        for (int i = numbers.length-1; i >= 0; i--) {
//            System.out.print(numbers[i]);
//            if (i != 0) {
//                System.out.print(", ");
//            }
//        }
        int sum = 0;
        for (int number : numbers) {
            sum += number;
        }
        double average = (double) sum / numbers.length;
        System.out.println("sum = " + sum);
        System.out.println("average = " + average);
    }
}
