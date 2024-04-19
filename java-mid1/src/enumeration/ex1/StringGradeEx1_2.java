package enumeration.ex1;


public class StringGradeEx1_2 {
    public static void main(String[] args) {
        int price = 10000;

        DiscountService discountService = new DiscountService();

        // 존재하지 않는등급
        int vip = discountService.discount("VIP", price);

        System.out.println("vip = " + vip);

        // 오타
        int diamondd = discountService.discount("DIAMONDD", price);
        System.out.println("diamondd = " + diamondd);

        // 소문자 입력
        int goldd = discountService.discount("gold", price);
        System.out.println("goldd = " + goldd);
    }

}
