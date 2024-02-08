package construct;

public class MemberInit {
    String name;
    int age;
    int grade;

//    public MemberInit(String name, int age, int grade) {
//        this.name = name;
//        this.age = age;
//        this.grade = grade;
//    }

    void initMember(String name, int age, int grade) {
        this.name = name;
        this.age = age;
        this.grade = grade;
    }
}
