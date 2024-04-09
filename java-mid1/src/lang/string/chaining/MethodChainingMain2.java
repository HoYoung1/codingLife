package lang.string.chaining;

public class MethodChainingMain2 {
    public static void main(String[] args) {
        ValueAdder adder = new ValueAdder();
//        adder.add(1);
//        adder.add(2);
//        adder.add(3);

        ValueAdder adder1 = adder.add(1);
        ValueAdder adder2 = adder1.add(2);
        ValueAdder adder3 = adder2.add(3);

        int result = adder3.getValue();
        System.out.println("result = " + result);
    }
}
