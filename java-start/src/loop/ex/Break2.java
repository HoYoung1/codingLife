package loop.ex;

public class Break2 {
    public static void main(String[] args) {
        int sum = 0;
        int i = 1;

        for (; sum < 10; i++) {
            sum += i;

        }
        System.out.println(i);

    }
}
