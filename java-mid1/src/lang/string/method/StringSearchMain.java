package lang.string.method;

public class StringSearchMain {
    public static void main(String[] args) {
        String str = "Hello, Java! welcome to Java world";

        System.out.println(str.contains("Java"));
        System.out.println("Java의 첫 인덱스 " + str.indexOf("Java"));
        System.out.println("인덱스 10부터 Java의 인덱스 : " + str.indexOf("Java", 10));
        System.out.println("자바의 마지막 index : "+ str.lastIndexOf("Java"));
    }
}
