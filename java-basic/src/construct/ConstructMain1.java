package construct;

public class ConstructMain1 {
    public static void main(String[] args) {
        MemberConstruct user1 = new MemberConstruct("user1", 15, 90);
        MemberConstruct user2 = new MemberConstruct("user2", 16, 80);

        MemberConstruct[] users = {user1, user2};

        for (MemberConstruct user : users) {
            System.out.println(user.name + " " + user.age + " " + user.grade);
        }
    }
}
