package lang.immutable.address;

public class MemberV2 {
    private String name;
    private ImmutableAddress address;

    public MemberV2(String name, ImmutableAddress address) {
        this.name = name;
        this.address = address;
    }

    @Override
    public String toString() {
        return "MemberV1{" +
                "name='" + name + '\'' +
                ", address=" + address +
                '}';
    }

    public ImmutableAddress getImmutableAddress() {
        return address;
    }

    public void setImmutableAddress(ImmutableAddress address) {
        this.address = address;
    }
}
