// 배열은 공변 제네릭은 불공변
// 배열은 실체화가 되지만 제네릭은 실체화가 되지않는다.
// 그래서 같이쓸때 여러가지 문제가 생길 수 있다.

import java.util.ArrayList;
import java.util.List;

public class Dangerous {

    static void dangerous(List<String>... stringLists) {
//        List<String>[] myList = new ArrayList<String>[10]; // 직접 만들수는 없지만 가변인수를 사용하면됨. 대신 경고가나옴

        List<Integer> intList = List.of(42);
        Object[] objects = stringLists;
        objects[0] = intList; // 힙 오염 발생
        ///asdfsadfsadfsdf

        String s = stringLists[0].get(0); // ClassCastException
    }

    public static void main(String[] args) {

        dangerous(List.of("There be dragons"));
    }
}
