package poly.basic;

public class CastingMain1 {
    public static void main(String[] args) {
        // 부모 인스턴스가 자식 인스턴스 참조(다형적 참조)
        Parent poly = new Child();
        // poly.childMethod();// 부모는 자식의 메소드를 호출 할 수 없다.

        // 다운 캐스팅
        Child child = (Child) poly;
        child.childMethod();
    }
}
