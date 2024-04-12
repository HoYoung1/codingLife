package lang.math;

import java.util.Random;

public class RandomMain {
    public static void main(String[] args) {
//        Random random = new Random();
        Random random = new Random(1); // seed 가 같으면 Random의 결과가 같다.

        int i = random.nextInt();
        System.out.println("i = " + i);

        double v = random.nextDouble();
        System.out.println("v = " + v);

        boolean b = random.nextBoolean();
        System.out.println("b = " + b);

        // 0~9 + 1 ---> 1~10
        int i1 = random.nextInt(10) + 1;
        System.out.println(i1);
    }
}
