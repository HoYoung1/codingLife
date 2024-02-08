package construct;

public class MemberConstruct {
    String name;
    int age;
    int grade;

    public MemberConstruct(String name, int age, int grade) {
        this.name = name;
        this.age = age;
        this.grade = grade;
    }

    public MemberConstruct(String name, int age) {
        this(name,age,50);
//        this.name = name;
//        this.age = age;
//        this.grade = 50;
    }
}
