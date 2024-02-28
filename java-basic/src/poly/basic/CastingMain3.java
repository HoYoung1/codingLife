package poly.basic;

// upcasting vs downCasting
public class CastingMain3 {
    public static void main(String[] args) {
        Child child = new Child();
        Parent parent1 = (Parent) child; // 업 캐스팅은 생략가능
        Parent parent2 = (Parent) child; // 업 캐스팅 생략

        parent1.parentMethod();
        parent2.parentMethod();
    }
}
