package lang.string.builder;

public class StringBuilderMain1_2 {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder();

        sb.append("A")
                .append("B")
                .append("C")
                .append("D")
                .insert(4, "java")
                .delete(4, 8)
                .reverse();
        System.out.println("sb = " + sb);

        String string = sb.toString();
        System.out.println(string);

    }
}
