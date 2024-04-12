package lang.wrapper.test;

public class WrapperTest1 {
    public static void main(String[] args) {
        String str1 = "10";
        String str2 = "20";

//        int i = Integer.valueOf(str1) + Integer.valueOf(str2);
        int i = Integer.parseInt(str1) + Integer.parseInt(str2);
        System.out.println("i = " + i);






    }
}
