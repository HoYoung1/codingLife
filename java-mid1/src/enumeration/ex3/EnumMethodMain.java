package enumeration.ex3;

import java.util.Arrays;

public class EnumMethodMain {
    public static void main(String[] args) {
        // 모든 ENUM 반환
        Grade[] values = Grade.values();
        System.out.println(Arrays.toString(values));

        for (Grade value : values) {
            System.out.println("value.name : " + value.name() + "value.ordinal : " + value.ordinal());
        }

        //String -> Enum 변환

//        String input = "gold"; // 예외 발생함
        String input = "GOLD";
        Grade gold = Grade.valueOf(input);
        System.out.println("gold = " + gold);
    }
}
