package time;

import java.time.LocalDate;
import java.time.Period;
import java.time.temporal.TemporalAmount;

public class PeriodMain {
    public static void main(String[] args) {
        // 생성
        Period period = Period.ofDays(10);
        System.out.println("period = " + period);

        LocalDate currentDate = LocalDate.of(2030, 1, 1);
        LocalDate plusDate = currentDate.plus(period);
        System.out.println("currentDate = " + currentDate);
        System.out.println("plusDate = " + plusDate);

        // 기간의 차이
        LocalDate startDate = LocalDate.of(2023, 1, 1);
        LocalDate endDate = LocalDate.of(2023, 4, 1);

        Period between = Period.between(startDate, endDate);
        System.out.println("between.getMonths() = " + between.getMonths());
        System.out.println("between.getDays() = " + between.getDays());


    }
}
