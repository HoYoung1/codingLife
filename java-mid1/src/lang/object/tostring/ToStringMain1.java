package lang.object.tostring;

public class ToStringMain1 {
    public static void main(String[] args) {
        Object o = new Object();
        String string = o.toString();

        // tostring 출력
        System.out.println(string);

        // object 출력
        System.out.println(o);
    }
}
