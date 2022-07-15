package chapter10;

public class BirdFactory {
    public static Bird createBird(Bird bird) {
        switch (bird.getType()) {
            case "유럽 제비" -> new EuropeanSwallow(bird);
            case "아프리카 제비" -> new AfricanSwallow(bird);
            case "노르웨이 파랑 앵무" -> new NorwegianBlueParrot(bird);
            default -> new Bird(bird);
        };
    }
}
