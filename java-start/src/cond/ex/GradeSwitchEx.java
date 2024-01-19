package cond.ex;

public class GradeSwitchEx {
    public static void main(String[] args) {
        String grade = "C";

        String result = switch (grade) {
            case "A" -> "탁원할 성과입니다";
            case "B" -> "좋은 성과입니다";
            case "C" -> "준수한 성과입니다";
            case "D" -> "향상이 필요합니다";
            default -> "잘못된 학점입니다";
        };

        System.out.println("result = " + result);
    }
}
