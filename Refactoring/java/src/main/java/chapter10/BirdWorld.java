package chapter10;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BirdWorld {
    public static void main(String[] args) {

    }

    public static Map plumages(List<Bird> birds) {
        Map<String, String> result = new HashMap<>();
        birds.forEach(bird -> result.put(bird.getName(), plumage(bird)));
        return result;
    }

    public static Map speeds(List<Bird> birds) {
        Map<String, Integer> result = new HashMap<>();
        birds.forEach(bird -> result.put(bird.getName(), airSpeedVelocity(bird)));
        return result;
    }

    public static String plumage(Bird bird) { // 깃털 상태
        return switch (bird.getType()) {
            case "유럽 제비" -> "보통이다";
            case "아프리카 제비" -> bird.numberOfCoconuts() > 2 ? "지쳤다" : "보통이다";
            case "노르웨이 파랑 앵무" -> bird.voltage() > 100 ? "그을렸다" : "예쁘다";
            default -> "알 수 없다";
        };
    }

    private static Integer airSpeedVelocity(Bird bird) { // 비행속도
        return switch (bird.getType()) {
            case "유럽 제비" -> 35;
            case "아프리카 제비" -> 40 - 2 * bird.numberOfCoconuts();
            case "노르웨이 파랑 앵무" -> bird.isNailed() ? 0 : 10 + bird.voltage() / 10;
            default -> null;
        };
    }
}
