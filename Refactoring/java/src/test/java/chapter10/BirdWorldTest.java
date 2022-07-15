package chapter10;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;
import java.util.Map;

class BirdWorldTest {
    List<Bird> birds = Arrays.asList(
            new Bird("hy", "유럽 제비", 3, 101, Boolean.FALSE),
            new Bird("hy2", "아프리카 제비", 3, 101, Boolean.FALSE),
            new Bird("hy3", "노르웨이 파랑 앵무", 3, 101, Boolean.TRUE)
    );

    @Test
    void plumages() {
        Assertions.assertEquals(BirdWorld.plumages(birds),
                Map.of(
                        "hy", "보통이다",
                        "hy2", "지쳤다",
                        "hy3", "그을렸다"
                )
        );
    }

    @Test
    void speeds() {
        Assertions.assertEquals(BirdWorld.speeds(birds),
                Map.of(
                        "hy", 35,
                        "hy2", 34,
                        "hy3", 0
                )
        );
    }
}