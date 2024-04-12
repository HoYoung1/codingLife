package lang.wrapper;

public class WrapperClassMain {
    public static void main(String[] args) {
        Integer i = new Integer(10);
        Integer i1 = Integer.valueOf(10);
        System.out.println("i = " + i);
        System.out.println("i1 = " + i1);

        Long l = Long.valueOf(10);
        System.out.println("l = " + l);

        Double v = Double.valueOf(12.5);
        System.out.println("v = " + v);

        System.out.println("내부 값 읽기");
        int i2 = i1.intValue();
        System.out.println("i2 = " + i2);

        long l1 = l.longValue();
        System.out.println("l1 = " + l1);

        System.out.println("비교");
        System.out.println("==" + (i == i1));
        System.out.println("equals" + (i.equals(i1)));
    }
}
