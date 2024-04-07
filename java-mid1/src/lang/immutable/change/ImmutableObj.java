package lang.immutable.change;

public class ImmutableObj {
    private final int value;

    public ImmutableObj(int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }

    public ImmutableObj add(int addValue) {
        return new ImmutableObj(this.value + addValue);
    }
}
