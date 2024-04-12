package lang.wrapper;

public class WrapperVsPrimitive {
    public static void main(String[] args) {
        int iterations = 1_000_000_000; // 반복횟수

        long startTime, endTime;

        // 기본형 Long 사용
        long sumPrimitive = 0;
        startTime = System.currentTimeMillis();
        for (int i = 0; i < iterations; i++) {
            sumPrimitive += 1;
        }
        System.out.println((System.currentTimeMillis() - startTime) + "ms");

        //래퍼 클래스 Long



        // 기본형 Long 사용
        Long sumWrapper = 0L;
        startTime = System.currentTimeMillis();
        for (int i = 0; i < iterations; i++) {
            sumWrapper += 1;
        }
        System.out.println((System.currentTimeMillis() - startTime) + "ms");


    }
}
