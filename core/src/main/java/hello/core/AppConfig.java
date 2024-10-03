package hello.core;

import hello.core.discount.DiscountPolicy;
import hello.core.discount.RateDiscountPolicy;
import hello.core.member.MemberRepository;
import hello.core.member.MemberServiceImpl;
import hello.core.member.MemoryMemberRepository;
import hello.core.order.OrderServiceImpl;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class AppConfig {

    @Bean
    public MemberServiceImpl memberService() {
        System.out.println("call AppConfig.memberService");
        return new MemberServiceImpl(memberRepository());
    }

    @Bean
    public MemberRepository memberRepository() {
        System.out.println("call AppConfig.memberRepository");
        return new MemoryMemberRepository();
    }

    @Bean
    public OrderServiceImpl orderService() {
        System.out.println("call orderService");
        return new OrderServiceImpl(memberRepository(), discountRepository());
//        return null;
    }

    @Bean
    public DiscountPolicy discountRepository() {
        System.out.println("call AppConfig.discountRepository");
//        return new FixDiscountPolicy();
        return new RateDiscountPolicy();
    }
}


