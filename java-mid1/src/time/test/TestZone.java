package time.test;

import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.ZonedDateTime;

public class TestZone {
    public static void main(String[] args) {
        LocalDateTime localDateTime = LocalDateTime.of(2024, 1, 1, 9, 0, 0);
//        ZonedDateTime  = ZonedDateTime.of(localDateTime, ZoneId.systemDefault());
        ZonedDateTime  seoulTime = ZonedDateTime.of(localDateTime, ZoneId.of("Asia/Seoul"));
        ZonedDateTime londonTime = seoulTime.withZoneSameInstant(ZoneId.of("Europe/London"));
        ZonedDateTime nyTime = seoulTime.withZoneSameInstant(ZoneId.of("America/New_York"));

        System.out.println("서울의 회의시간 = " + seoulTime);
        System.out.println("런던의 회의시간 = " + londonTime);
        System.out.println("뉴욕의 회의시간 = " + nyTime);
    }
}
