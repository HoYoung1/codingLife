package chapter10;

public class Bird {
    private String name;
    private String type;
    private Integer coconuts;
    private Integer voltage;
    private Boolean isNailed;

    public Bird(String name, String type, Integer coconuts, Integer voltage, Boolean isNailed) {
        this.name = name;
        this.type = type;
        this.coconuts = coconuts;
        this.voltage = voltage;
        this.isNailed = isNailed;
    }

    public String getName() {
        return name;
    }

    public String getType() {
        return type;
    }

    public Integer numberOfCoconuts() {
        return 5; // hard code
    }

    public Integer voltage() {
        return 120; // hard code
    }

    public Boolean isNailed() {
        return Boolean.TRUE; // hard code
    }
}
