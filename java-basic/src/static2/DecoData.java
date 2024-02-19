package static2;

public class DecoData {
    private int instanceValue;
    private static int staticValue;

    public static void staticCall() {
        // instanceValue++; static method는 member 변수에 접근할 수 없다.
        staticValue++; // 정적 변수 접근
        staticMethod(); // 정적 메소드 접근
    }

    public void instanceCall() {
        instanceValue++;
        instanceMethod();

        staticValue++; // 정적 변수 접근
        staticMethod(); // 정적 메소드 접근
    }
    private void instanceMethod() {
        System.out.println("instanceValue = " + instanceValue);
    }

    private static void staticMethod() {
        System.out.println("staticValue = " + staticValue);
    }
}
