package hello.core.singletone;

import hello.core.AppConfig;
import hello.core.member.MemberRepository;
import hello.core.member.MemberService;
import hello.core.member.MemberServiceImpl;
import hello.core.order.OrderServiceImpl;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class ConfigurationSingletonTest {

    @Test
    void configurationTest() {
        AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);
        MemberServiceImpl bean1 = ac.getBean(MemberServiceImpl.class);
        OrderServiceImpl bean2 = ac.getBean(OrderServiceImpl.class);

        MemberRepository memberRepository1 = bean1.memberRepository();
        System.out.println("bean1 = " + memberRepository1);
        MemberRepository memberRepository2 = bean2.memberRepository();
        System.out.println("bean2 = " + memberRepository2);

        MemberRepository bean3 = ac.getBean(MemberRepository.class);
        System.out.println("bean3 = " + bean3);

        Assertions.assertThat(memberRepository1).isSameAs(memberRepository2);
        Assertions.assertThat(memberRepository2).isSameAs(bean3);
        Assertions.assertThat(bean3).isSameAs(memberRepository1);

        System.out.println("bean3 = " + bean3.getClass());
    }

    @Test
    void configurationDeepp() {
        AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);
        AppConfig bean = ac.getBean(AppConfig.class);
        System.out.println("bean.getClass() = " + bean.getClass());
    }
}
