package construct;

public class MemberInitMain3 {
    public static void main(String[] args) {
        MemberInit memberInit1 = new MemberInit();
        memberInit1.initMember( "user1", 16, 80);

        MemberInit memberInit2 = new MemberInit();
        memberInit2.initMember( "user2", 16, 80);

        MemberInit[] members = {memberInit1, memberInit2};

        for (MemberInit member : members) {
            System.out.println("" + member.name);
        }
    }

    static void initMember(MemberInit member, String name, int age, int grade) {
        member.name = name;
        member.age = age;
        member.grade = grade;
    }

}
