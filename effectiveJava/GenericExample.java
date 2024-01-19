import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class GenericExample<T> {
    private int size;
    Object[] elementData;

    public <T> T[] toArray(T[] a) {
        if (a.length < size)
            // Make a new array of a's runtime type, but my contents:
            return (T[]) Arrays.copyOf(elementData, size, a.getClass());
        System.arraycopy(elementData, 0, a, 0, size);
        if (a.length > size)
            a[size] = null;
        return a;
    }

    public static <T> T exampleGeneric(T c){
        return c;
    }

    public static <T> T example2() {
        int c = 1;
        return (T) exampleGeneric(1);
    }

//    public static double example2() {
//        int c = 1;
//        return (double) exampleGeneric(1);
//    }
}
