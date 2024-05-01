package time;

import java.time.LocalDateTime;
import java.time.temporal.ChronoField;

public class GetTimeMain {
    public static void main(String[] args) {
        LocalDateTime dt = LocalDateTime.of(2030, 1, 1, 13, 30, 59);
        int year = dt.get(ChronoField.YEAR);
        System.out.println("year = " + year);

        System.out.println("month = " + dt.get(ChronoField.MONTH_OF_YEAR));
        System.out.println("day = " + dt.get(ChronoField.DAY_OF_MONTH));
        System.out.println("hour = " + dt.get(ChronoField.HOUR_OF_DAY));
        System.out.println("minute = " + dt.get(ChronoField.MINUTE_OF_HOUR));
        System.out.println("second = " + dt.get(ChronoField.SECOND_OF_MINUTE));

        System.out.println("편의 메서드 제공");
        System.out.println("month = " + dt.getMonthValue());
        System.out.println("day = " + dt.getDayOfMonth());
        System.out.println("hour = " + dt.getHour());
        System.out.println("minute = " + dt.getMinute());
        System.out.println("second = " + dt.getSecond());

        System.out.println("편의 메서드에 없음 ");
        System.out.println(dt.get(ChronoField.MINUTE_OF_DAY));
        System.out.println(dt.get(ChronoField.SECOND_OF_DAY));
    }
}
