package nested.nested.anonymous.ex;

import java.util.Random;

public class Ex1MainSelfRefactor {
    public static void hello(Ex1Interface ex1Interface) {
        System.out.println("프로그램 시작");

        // 코드 조각 시작
        ex1Interface.method1();
        // 코드 조각 종료

        System.out.println("프로그램 종료");
    }

    public static void main(String[] args) {
        hello(new Ex1Interface() {
            @Override
            public void method1() {
                int randomValue = new Random().nextInt(6) + 1;
                System.out.println("randomValue = " + randomValue);
            }
        });

        hello(new Ex1Interface() {
            @Override
            public void method1() {
                for (int i = 0; i < 3; i++) {
                    System.out.println("i =" + i);
                }
            }
        });

    }


}
