package lang.object.poly;

public class ObjectPolyExample2 {
    public static void main(String[] args) {
        Dog dog = new Dog();
        Car car = new Car();
        Object o = new Object(); // Object 인스턴스도 만들 수 있음

        Object[] objects = {dog, car, o};
//        Object[] objects = new Object[3];

        size(objects);

//        Dog[] dogs = {new Dog(), new Dog()};
//        size(dogs);

    }

    private static void size(Object[] objects) {
        System.out.println("전달된 객체의 수는 : " + objects.length);
    }
}
