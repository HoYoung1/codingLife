package time;

import java.time.ZoneId;
import java.util.Set;

public class ZoneIdMain {
    public static void main(String[] args) {
        for (String availableZoneId : ZoneId.getAvailableZoneIds()) {
//            System.out.println(availableZoneId);
            ZoneId zoneId = ZoneId.of(availableZoneId);
            System.out.println(zoneId + " | " + zoneId.getRules());

            ZoneId zoneId1 = ZoneId.systemDefault();
            ZoneId seoulZoneId = ZoneId.of("Asia/Seoul");

            System.out.println(zoneId1);
            System.out.println(seoulZoneId);
        }
    }
}
