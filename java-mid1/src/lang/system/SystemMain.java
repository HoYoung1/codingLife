package lang.system;

import java.util.Arrays;
import java.util.Map;

public class SystemMain {
    public static void main(String[] args) {
        // 1. 현재 시간을 ms로
        long l = System.currentTimeMillis();
        System.out.println(l);

        // 2. 현재 시간을 ns로
        long l1 = System.nanoTime();
        System.out.println(l1);

        // 3. 환경변수
        Map<String, String> getenv = System.getenv();
        System.out.println("getenv = " + getenv);

        // 4. 시스템 속성을 읽는다
        System.out.println(System.getProperties());
        System.out.println(System.getProperty("java.version"));

        // 5. 배열을 고속으로 복사한다.
        char[] originalArray = {'h', 'e', 'l', 'l', 'o'};
        char[] copiedArray = new char[5];
        System.arraycopy(originalArray,0,copiedArray,0,originalArray.length);

        // 6. 배열 출력
        System.out.println(Arrays.toString(originalArray));
        System.out.println(Arrays.toString(copiedArray));

        // 프로그램 출력
        System.exit(0);
        System.out.println("hello");
    }
}
