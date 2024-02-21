package final1;

public class FinalLocalMain {
    public static void main(String[] args) {
        // final 지역 변수
        final int data1;
        data1 = 10; // 최초 한번만 할당 가능
//        data2 = 20; // 컴파일 오류

        final int data2 = 10;
//        data2 = 20; // 컴파일 오류
        method(20);


    }

    static void method(final int parameter) {
//        parameter = 30; // 컴파일오류
    }
}
