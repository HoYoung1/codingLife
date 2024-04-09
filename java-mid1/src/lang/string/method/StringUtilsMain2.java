package lang.string.method;

public class StringUtilsMain2 {
    public static void main(String[] args) {
        int num = 1000;
        boolean bool = true;
        Object o = new Object();
        String str = "Hello, Java";

        // format 메서드
        String format = String.format("num : %d, bool: %b, str: %s", num, bool, str);
        System.out.println(format);

        String format1 = String.format("%.2f", 10.1234);
        System.out.println(format1);

        //printf
        System.out.printf("%.2f", 10.1234);

        //matches 메서드

        String regex = "Hello, (Java|World)";
        System.out.println(str.matches(regex));
    }
}
