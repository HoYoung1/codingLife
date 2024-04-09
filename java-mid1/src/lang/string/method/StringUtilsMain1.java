package lang.string.method;

public class StringUtilsMain1 {
    public static void main(String[] args) {
        int num = 1000;
        boolean bool = true;
        Object o = new Object();
        String str = "Hello, Java";

        // valueOf 메서드
        String numString = String.valueOf(num);
        System.out.println("숫자의 문자열 값 : " + numString);

        String boolString = String.valueOf(bool);
        System.out.println("boolean 문자열 값 : " + boolString);

        String objectString = String.valueOf(o);
        System.out.println("objectString 문자열 값 : " + objectString);

        // 문자 + x -> 문자
        String numString2 = "" + num;
        System.out.println("빈문자열 + num " + numString2);

        // toCharArray
        char[] strCharArray = str.toCharArray();
        System.out.println("문자열을 문자 배열로 전환 " + strCharArray);

        for (char c : strCharArray) {
            System.out.print(c);
        }


    }
}
