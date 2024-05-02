package nested.nested.inner;

public class InnerOuter {
    private static int outClassValue = 3;
    private int outInstanceValue = 2;

    class Inner {
        private int innerInstanceValue = 1;

        public void print() {
            // 자기 자신에 접근
            System.out.println("innerInstanceValue = " + innerInstanceValue);

            // outer 클래스의 멤버 변수에 접근
            System.out.println("outInstanceValue = " + outInstanceValue);

            // outer 클래스의 static 변수에 접근
            System.out.println("outClassValue = " + outClassValue);
        }
    }
}
