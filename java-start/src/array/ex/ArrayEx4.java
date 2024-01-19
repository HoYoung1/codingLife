package array.ex;

import java.util.Scanner;

public class ArrayEx4 {
    public static void main(String[] args) {
        int[] numbers = new int[5];
        Scanner scanner = new Scanner(System.in);


        System.out.println("5개의 정수를 입력하세요");
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
