package time.test;

import java.awt.event.AdjustmentListener;
import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.temporal.TemporalAdjuster;
import java.time.temporal.TemporalAdjusters;

public class TestAdjusters {
    public static void main(String[] args) {
        int year = 2024;
        int month = 1;

        // 코드 작성
        LocalDate localDate = LocalDate.of(2024, 1, 1);

        DayOfWeek firstDayOfWeek = localDate.getDayOfWeek();
        DayOfWeek lastDayOfWeek = localDate.with(TemporalAdjusters.lastDayOfMonth()).getDayOfWeek();
        System.out.println("firstDayOfWeek = " + firstDayOfWeek);
        System.out.println("lastDayOfWeek = " + lastDayOfWeek);


    }
}
