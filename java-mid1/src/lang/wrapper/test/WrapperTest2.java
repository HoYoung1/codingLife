package lang.wrapper.test;

public class WrapperTest2 {
    public static void main(String[] args) {
        String[] array = {"1.5", "2.5", "3.0"};

        // 코드 작성
        Double sum = 0.0;
        for (String s : array) {
            sum += Double.parseDouble(s);
        }
        System.out.println(sum);
    }
}
