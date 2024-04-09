package lang.string.test;

public class TestString6 {
    public static void main(String[] args) {
        String s = "Hello Java, Hello World , Hello goodbye";
        String key = "Hello";

        int beforeIndex = s.indexOf(key);
        int count = 0;
        while (beforeIndex != -1) {
            beforeIndex = s.indexOf(key, beforeIndex + 1);
            count += 1;
        }
        System.out.println(count);
    }

}
