package time;

import java.time.Duration;
import java.time.LocalTime;

public class DurationMain {
    public static void main(String[] args) {
        Duration duration = Duration.ofMinutes(30);
        System.out.println("duration = " + duration);

        LocalTime lt = LocalTime.of(1, 0);
        System.out.println("lt = " + lt);

        // 계산에 사용
        LocalTime plus = lt.plus(duration);
        System.out.println("plus = " + plus);

        // 시간 차이
        LocalTime start = LocalTime.of(9, 0);
        LocalTime end = LocalTime.of(10, 0);

        Duration between = Duration.between(start, end);
        System.out.println("between = " + between);

        System.out.println("between.getSeconds() = " + between.getSeconds());
        System.out.println("between.toMinutes() = " + between.toMinutes());
    }
}
