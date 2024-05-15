package nested.nested.anonymous.ex;

public class Ex0MainSelfRefactor {
    public static void helloJava() {
        System.out.println("프로그램 시작");
        System.out.println("Hello Java");
        System.out.println("프로그램 종료");
    }

    public static void helloSpring() {
        System.out.println("프로그램 시작");
        System.out.println("Hello Spring");
        System.out.println("프로그램 종료");
    }

    public static void helloWith(String x) {
        System.out.println("프로그램 시작");
        System.out.println(x);
        System.out.println("프로그램 종료");
    }

    public static void main(String[] args) {
//        helloJava();
//        helloSpring();

        helloWith("Hello Java");
        helloWith("Hello Spring");
    }
}
