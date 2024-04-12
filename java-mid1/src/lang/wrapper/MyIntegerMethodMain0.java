package lang.wrapper;

public class MyIntegerMethodMain0 {
    public static void main(String[] args) {
        int value = 10;
        int i1 = compareTo(value, 5);
        int i2 = compareTo(value,10);
        int i3 = compareTo(value, 15);
        System.out.println("i = " + i1);
        System.out.println("i = " + i2);
        System.out.println("i = " + i3);
    }

    private static int compareTo(int value, int target) {
        if (value < target) {
            return -1;
        } else if (value > target) {
            return 1;
        }
        return 0;
    }
}
