package nested.nested;

public class NestedOuter {
    private static int outClassValue = 3;
    private int outInstanceValue = 2;

    static class Nested {
        private int nestedInstanceValue = 1;

        public void print() {
            // 자신의 멤버에 접근
            System.out.println("nestedInstanceValue = " + nestedInstanceValue);

            // 바깥 클래스의 인스턴스 멤버에 접근할 수 없다.
 //            System.out.println("outInstanceValue = " + outInstanceValue);

            // 바깥 클래스의 static 멤버에 접근. private 도 접근 가능
            System.out.println("outClassValue = " + outClassValue);
            System.out.println("outClassValue = " + NestedOuter.outClassValue);
        }
    }
}
