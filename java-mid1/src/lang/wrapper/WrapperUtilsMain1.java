package lang.wrapper;

public class WrapperUtilsMain1 {
    public static void main(String[] args) {
        Integer i = Integer.valueOf(10);
        Integer i1 = Integer.valueOf("10");
        int i2 = Integer.parseInt("10");

        int compareResult = i1.compareTo(20);
        System.out.println("compareResult = " + compareResult);

        System.out.println(Integer.sum(10, 20));
        System.out.println(Integer.min(30, 40));
        System.out.println(Integer.max(20, 10));
    }
}
