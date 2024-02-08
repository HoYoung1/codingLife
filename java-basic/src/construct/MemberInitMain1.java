package construct;

public class MemberInitMain1 {
    public static void main(String[] args) {
        MemberInit memberInit1 = new MemberInit();
        memberInit1.name = "user1";
        memberInit1.age = 15;
        memberInit1.grade = 90;

        MemberInit memberInit2 = new MemberInit();
        memberInit2.name = "user2";
        memberInit2.age = 16;
        memberInit2.grade = 80;

        MemberInit[] members = {memberInit1, memberInit2};

        for (MemberInit member : members) {
            System.out.println("" + member.name);
        }
    }

}
