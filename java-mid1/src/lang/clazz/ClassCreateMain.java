package lang.clazz;

import java.lang.reflect.InvocationTargetException;

public class ClassCreateMain {
    public static void main(String[] args) throws Exception {
//        Class helloClass = Hello.class;
        Class helloClass = Class.forName("lang.clazz.Hello");
        Hello o = (Hello) helloClass.getDeclaredConstructor().newInstance();
        System.out.println(o.getHello());
    }
}
