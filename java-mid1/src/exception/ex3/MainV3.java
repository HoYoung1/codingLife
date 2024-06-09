package exception.ex3;

import exception.ex2.NetworkServiceV2_5;
import exception.ex2_self.NetworkClientExceptionV2_Self;

import java.util.Scanner;

public class MainV3 {
    public static void main(String[] args) throws NetworkClientExceptionV2_Self {
//        NetworkServiceV3 networkService = new NetworkServiceV3();
        NetworkServiceV3_2 networkService = new NetworkServiceV3_2();

        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.print("전송할 문자: ");
            String input = scanner.nextLine();
            if (input.equals("exit")) {
                break;
            }
            networkService.sendMessage(input);
            System.out.println();
        }
        System.out.println("프로그램을 정상 종료합니다.");
    }
}
