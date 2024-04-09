package lang.string.test;

public class TestString10 {
    public static void main(String[] args) {
        String s = "apple,banana,mango";
        String[] split = s.split(",");
        for (String string : split) {
            System.out.println(string);
        }
        System.out.println(String.join("->", split));
    }

}
