package lang.string.method;

public class StringChangeMain1 {
    public static void main(String[] args) {
        String str = "Hello, Java! welcome to Java";

        System.out.println("인덱스 7부터의 부분 문자열");
        System.out.println(str.substring(7));

        System.out.println("인덱스 7부터 12까지 부분 문자열");
        System.out.println(str.substring(7, 12));

        System.out.println("문자열 결합 : " + str.concat("!!!"));

        System.out.println("'Java'를 World로 교체 " + str.replace("Java", "World"));
        System.out.println("첫번째 Java를 Wolrd로 교체" + str.replaceFirst("Java", "World"));
    }
}
