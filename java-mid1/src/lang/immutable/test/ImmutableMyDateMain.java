package lang.immutable.test;

public class ImmutableMyDateMain {
    public static void main(String[] args) {
        ImmutableMyDate myDate1 = new ImmutableMyDate(2024,1,1);
        ImmutableMyDate myDate2 = myDate1;

        System.out.println("myDate1 = " + myDate1);
        System.out.println("myDate2 = " + myDate2);

        System.out.println("2025 -> date1");
        myDate1.withYear(2025);

        System.out.println("myDate1 = " + myDate1);
        System.out.println("myDate2 = " + myDate2);
    }
}
