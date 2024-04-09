package lang.string.equals;

public class StringEqualsMain2 {
    public static void main(String[] args) {
        String str1 = new String("Hello");
        String str2 = new String("Hello");
        System.out.println("메서드 호출 비교1" + isSame(str1, str2));

        String str3 = "hello";
        String str4 = "hello";
        System.out.println("메서드 호출 비교1" + isSame(str3, str4));
    }


    private static boolean isSame(String x, String y) {
        return x.equals(y);
    }
}
