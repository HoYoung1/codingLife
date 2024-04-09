package lang.string.test;

public class TestString4 {
    public static void main(String[] args) {
        String s = "hello.txt";
        int beginIndex = s.indexOf(".txt");
        System.out.println(s.substring(0,beginIndex));
        System.out.println(s.substring(beginIndex));
    }

}
