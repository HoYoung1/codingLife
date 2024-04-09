package lang.string.test;

public class TestString9 {
    public static void main(String[] args) {
        String s = "hello@example.com";
        String[] split = s.split("@");
        for (String string : split) {
            System.out.println(string);
        }
    }

}
