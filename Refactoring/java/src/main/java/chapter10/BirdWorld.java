package chapter10;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class BirdWorld {
    public static void main(String[] args) {

    }

    public static Map plumages(List<Bird> birds) {
        Map<String, String> result = new HashMap<>();
        birds.forEach(bird -> result.put(bird.getName(), bird.plumage()));
        return result;
    }

    public static Map speeds(List<Bird> birds) {
        Map<String, Integer> result = new HashMap<>();
        birds.forEach(bird -> result.put(bird.getName(), Bird.airSpeedVelocity(bird)));
        return result;
    }
}
