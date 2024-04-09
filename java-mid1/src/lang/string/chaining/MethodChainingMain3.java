package lang.string.chaining;

import java.util.ArrayList;

public class MethodChainingMain3 {
    public static void main(String[] args) {
        ValueAdder adder = new ValueAdder();

        adder.add(1).add(2).add(3);

        int result = adder.getValue();
        System.out.println("result = " + result);

        ArrayList<Object> objects = new ArrayList<>();

    }
}
