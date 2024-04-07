package lang.immutable.change;

public class ImmutableMain1 {
    public static void main(String[] args) {
        ImmutableObj obj = new ImmutableObj(10);
        ImmutableObj obj2 = obj.add(20);

        System.out.println("obj2.getValue() = " + obj2.getValue());

    }
}
