package lang.string.method;

public class StringSplitJoinMain {
    public static void main(String[] args) {
        String str = "Apple, Banana, Orange";
        // split()

        String[] split = str.split(", ");
        for (String s : split) {
            System.out.println(s);
        }

        System.out.println(String.join("-", split));

    }
}
