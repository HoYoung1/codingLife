package time;

import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.ZonedDateTime;

public class ZonedDateTimeMain {
    public static void main(String[] args) {
        ZonedDateTime nowZdt = ZonedDateTime.now();
        System.out.println("nowZdt = " + nowZdt);

        LocalDateTime ldt = LocalDateTime.of(2030, 1, 1, 13, 30, 50);
        ZonedDateTime zdt1 = ZonedDateTime.of(ldt, ZoneId.of("Asia/Shanghai"));
        System.out.println("zdt1 = " + zdt1);

        ZonedDateTime jdt2 = ZonedDateTime.of(2023, 11, 23, 3, 5, 30,3, ZoneId.of("Asia/Seoul"));
        System.out.println("jdt2 = " + jdt2);

        ZonedDateTime utc = jdt2.withZoneSameInstant(ZoneId.of("UTC"));
        System.out.println("utc = " + utc);


    }
}
