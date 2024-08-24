package hello.core.singletone;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;

import static org.junit.jupiter.api.Assertions.*;

class StatefulServiceTest {

    private AnnotationConfigApplicationContext ac =
            new AnnotationConfigApplicationContext(TestConfig.class);

    @Test
    void statefulServiceSingleton() {
        StatefulService statefulService1 = ac.getBean("statefulService", StatefulService.class);
        StatefulService statefulService2 = ac.getBean("statefulService", StatefulService.class);

        // 가정 : threadA에서 10000원
        statefulService1.order("nameA", 10000);
        // 가정 : threadB에서 20000원
        statefulService2.order("nameB", 20000);

        Assertions.assertThat(statefulService1.getPrice()).isEqualTo(20000);
    }

    static class TestConfig {
        @Bean
        public StatefulService statefulService() {
            return new StatefulService();
        }
    }
}