package hello.core.scan;

import hello.core.AutoAppConfig;
import hello.core.member.MemberRepository;
import hello.core.member.MemberService;
import org.junit.jupiter.api.Test;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import static org.assertj.core.api.Assertions.assertThat;

public class AutoAppConfigTest {

    @Test
    void basicScan() {
        AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AutoAppConfig.class);

        MemberRepository bean = ac.getBean(MemberRepository.class);
        assertThat(bean).isInstanceOf(MemberRepository.class);

        MemberService bean1 = ac.getBean(MemberService.class);
        assertThat(bean1).isInstanceOf(MemberService.class);
    }


}
