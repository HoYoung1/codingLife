package lang.wrapper;

public class MyIntegerNullMain1 {
    public static void main(String[] args) {
//        int[] intArr = {-1, 0, 1, 2, 3};
        MyInteger[] intArr = {
                new MyInteger(-1),
                new MyInteger(0),
                new MyInteger(1),
                new MyInteger(2)};

        System.out.println("value = " + findValue(intArr, -1));
        System.out.println("value = " + findValue(intArr, 0));
        System.out.println("value = " + findValue(intArr, 1));
        System.out.println("value = " + findValue(intArr, 2));
        System.out.println("value = " + findValue(intArr, 100));
    }

    private static MyInteger findValue(MyInteger[] intArr, int target) {
        for (MyInteger value : intArr) {
            if (value.getValue() == target) {
                return value;
            }
        }
        return null;
    }
}
