package lang.wrapper.test;

public class WrapperTest4 {
    public static void main(String[] args) {
        String str = "100";

        Integer i = Integer.valueOf(str);
        System.out.println(i);

        int i1 = i;
        System.out.println(i1);

        Integer i2 = i1;
        System.out.println(i2);
    }
}
