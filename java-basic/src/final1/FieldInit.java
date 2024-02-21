package final1;

public class FieldInit {
    static final int CONST_VALUE = 10;
    final int value = 10;

    public FieldInit() {
//        value = 20;  // 이미 초기화했기때문에 안됨
    }
}
