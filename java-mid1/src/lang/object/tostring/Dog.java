package lang.object.tostring;

public class Dog {
    private String dogName;
    private int age;

    public Dog(String name, int age) {
        this.dogName = name;
        this.age = age;
    }


//    @Override
//    public String toString() {
////        return super.toString();
//        return "dogName=" + dogName + "/" + "age=" + age;
//    }


    @Override
    public String toString() {
        return "Dog{" +
                "dogName='" + dogName + '\'' +
                ", age=" + age +
                '}';
    }
}
