package operator;

public class Operator2 {
    public static void main(String[] args) {
        String result = "Hello" + "World";
        System.out.println("result = " + result);

        String s1 = "Hello";
        String s2 = "World";
        String result2 = s1 + s2;
        System.out.println("result2 = " + result2);

        // 문자열과 숫자 더하기
        String result3 = "a + b " + 10;
        System.out.println("result3 = " + result3);

        // 문자열과 숫자 더하기2
        int num = 20;
        String str = "a + b = ";
        String result4 = str + "a + b = 40";
        System.out.println(str + result4 + num);


    }
}
