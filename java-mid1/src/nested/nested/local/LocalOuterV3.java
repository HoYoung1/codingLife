package nested.nested.local;

import java.lang.reflect.Field;

public class LocalOuterV3 {
    private int outInstanceVar = 3;

    public Printer process(int paramVar) {
        int localVar = 1; // 지역 변수는 스택 프레임이 종료되는 순간 함께 제거된다.

        class LocalPrint implements Printer {
            int value = 0;

            public void printData() {
                System.out.println("value = " + value);
                System.out.println("localVar = " + localVar);
                System.out.println("paramVar = " + paramVar);
                System.out.println("outInstanceVar = " + outInstanceVar);
            }

            // 인스턴스는 지역 변수보다 더 오래 살아남는다.
            @Override
            public void print() {
                printData();
            }

        }

        LocalPrint printer = new LocalPrint();
//        printer.printData(); // 여기서 실행하지 않고
        return printer;
    }

    public static void main(String[] args) {
        LocalOuterV3 localOuterV1 = new LocalOuterV3();
        Printer printer = localOuterV1.process(2);
        printer.print();

        Field[] fields = printer.getClass().getFields();
        for (Field field : fields) {
            System.out.println(field);
        }
    }
}
