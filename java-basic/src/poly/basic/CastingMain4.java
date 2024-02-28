package poly.basic;

public class CastingMain4 {
    public static void main(String[] args) {
        Parent parent1 = new Child();
        Child child = (Child) parent1;
        child.childMethod();


        Parent parent2 = new Parent();
        Child child1 = (Child) parent2; // ClassCastException
        child1.childMethod(); // 실행불가
    }
}
