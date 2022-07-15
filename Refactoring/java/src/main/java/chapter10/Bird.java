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

    public static String plumage(Bird bird) { // 깃털 상태
        return switch (bird.getType()) {
            case "유럽 제비" -> "보통이다";
            case "아프리카 제비" -> bird.numberOfCoconuts() > 2 ? "지쳤다" : "보통이다";
            case "노르웨이 파랑 앵무" -> bird.voltage() > 100 ? "그을렸다" : "예쁘다";
            default -> "알 수 없다";
        };
    }

    public static Integer airSpeedVelocity(Bird bird) { // 비행속도
        return switch (bird.getType()) {
            case "유럽 제비" -> 35;
            case "아프리카 제비" -> 40 - 2 * bird.numberOfCoconuts();
            case "노르웨이 파랑 앵무" -> bird.isNailed() ? 0 : 10 + bird.voltage() / 10;
            default -> null;
        };
    }

    public String getName() {
        return name;
    }

    public String getType() {
        return type;
    }

    public Integer numberOfCoconuts() {
        return coconuts; // hard code
    }

    public Integer voltage() {
        return voltage; // hard code
    }

    public Boolean isNailed() {
        return Boolean.TRUE; // hard code
    }
}
