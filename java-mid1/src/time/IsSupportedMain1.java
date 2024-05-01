package time;

import java.time.LocalDate;
import java.time.temporal.ChronoField;

public class IsSupportedMain1 {
    public static void main(String[] args) {
        LocalDate now = LocalDate.now();
        int i = now.get(ChronoField.SECOND_OF_MINUTE);

        System.out.println("i = " + i);
    }
}
