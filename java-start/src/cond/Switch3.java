package cond;

public class Switch3 {
    public static void main(String[] args) {
        int grade = 2;

        switch (grade) {
            case 1:
                System.out.println("1");
                break;
            case 2:
            case 3:
                System.out.println("3");
                break;
            default:
                System.out.println("3");
                break;
        }
    }
}
