package poly.overriding;

public class Child extends Parent {
    public String value = "child";

    @Override
    public void method() {
        super.method();
        System.out.println("Child.method");
    }
}
