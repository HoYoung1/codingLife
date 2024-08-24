package hello.core.singletone;

import hello.core.AppConfig;
import hello.core.member.MemberService;
import hello.core.member.MemberServiceImpl;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class SingletonServiceTest {


    @Test
    void pureContainer() {
        AppConfig appConfig = new AppConfig();
        //1. 조회 : 호출할 때 마다 객체를 생성
        MemberServiceImpl memberService1 = appConfig.memberService();

        //2. 조회 : 호출할 때 마다 객체를 생성
        MemberServiceImpl memberService2 = appConfig.memberService();

        // 참조 값이 다른 것을 확인
        System.out.println("memberService1 = " + memberService1);
        System.out.println("memberService2 = " + memberService2);

        // memberservice1 != memberservice2
        Assertions.assertThat(memberService1).isNotSameAs(memberService2);
    }

    @Test
    void singletonServiceTest() {
        SingletonService instance1 = SingletonService.getInstance();
        SingletonService instance2 = SingletonService.getInstance();

        Assertions.assertThat(instance1).isSameAs(instance2);
    }

    @Test
    void springContainer() {
//        AppConfig appConfig = new AppConfig();
        AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);

        MemberService memberService1 = ac.getBean("memberService", MemberService.class);
        MemberService memberService2 = ac.getBean("memberService", MemberService.class);

        System.out.println("memberService1 = " + memberService1);
        System.out.println("memberService2 = " + memberService2);

        Assertions.assertThat(memberService1).isSameAs(memberService2);

    }
}
