package time;

import java.time.LocalTime;

public class LocalTimeMain {
    public static void main(String[] args) {
        LocalTime now = LocalTime.now();
        LocalTime ofTime = LocalTime.of(9, 10, 30);
//        LocalTime.of(9, 10, 30)
        System.out.println("현재 시간 = " + now);
        System.out.println("ofTime = " + ofTime);

        // 계산(불변)
        LocalTime ofTimePlus = ofTime.plusSeconds(30);
        System.out.println("ofTimePlus = " + ofTimePlus);
    }
}
