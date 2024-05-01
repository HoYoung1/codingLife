package time.test;

import java.time.Duration;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.Period;
import java.time.temporal.TemporalAmount;

public class TestPlus {
    public static void main(String[] args) {
        // 2024년 1월 1일 0시 0분 0초
        // 1년 2개월 3일 4시간 후의 시각을 찾아라

        LocalDateTime localDateTime = LocalDateTime.of(2024, 1, 1, 0, 0, 0);
        LocalDateTime plus = localDateTime
                .plus(Period.of(1, 2, 3))
                .plus(Duration.ofDays(3))
                .plus(Duration.ofHours(4));
        System.out.println("plus = " + plus);

    }
}
