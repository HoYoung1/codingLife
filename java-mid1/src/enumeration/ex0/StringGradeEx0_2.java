package enumeration.ex0;

public class StringGradeEx0_2 {
    public static void main(String[] args) {
        int price = 10000;

        DiscountService discountService = new DiscountService();

        int basic = discountService.discount("BASIC", price);
        int gold = discountService.discount("GOLD", price);
        int diamond = discountService.discount("DIAMOND", price);

        // 존재하지 않는등급
        int vip = discountService.discount("VIP", price);

        System.out.println("basic = " + basic);
        System.out.println("gold = " + gold);
        System.out.println("diamond = " + diamond);
        System.out.println("vip = " + vip);

        // 오타
        int diamondd = discountService.discount("DIAMONDD", price);
        System.out.println("diamondd = " + diamondd);

        // 소문자 입력
        int goldd = discountService.discount("gold", price);
        System.out.println("goldd = " + goldd);
    }

}
