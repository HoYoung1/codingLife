package nested.nested.anonymous;

import nested.nested.local.Printer;

public class AnonymousOuter {
    private int outInstanceVar = 3;

    public void process(int paramVar) {
        int localVar = 1;

//        class LocalPrint implements Printer {
//            int value = 0;
//
//            public void printData() {
//                System.out.println("value = " + value);
//                System.out.println("localVar = " + localVar);
//                System.out.println("paramVar = " + paramVar);
//                System.out.println("outInstanceVar = " + outInstanceVar);
//            }
//
//            @Override
//            public void print() {
//                printData();
//            }
//        }

//        LocalPrint printer = new LocalPrint();

        Printer printer = new Printer() {
            int value = 0;

            @Override
            public void print() {
                System.out.println("value = " + value);
                System.out.println("localVar = " + localVar);
                System.out.println("paramVar = " + paramVar);
                System.out.println("outInstanceVar = " + outInstanceVar);

            }
        };
        printer.print();

        System.out.println("printer.getClass() = " + printer.getClass());
    }

    public static void main(String[] args) {
        AnonymousOuter localOuterV1 = new AnonymousOuter();
        localOuterV1.process(2);
    }
}
