package hello.core;

import hello.core.discount.FixDiscountPolicy;
import hello.core.member.MemberServiceImpl;
import hello.core.member.MemoryMemberRepository;
import hello.core.order.OrderServiceImpl;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class AppConfig {

    @Bean
    public MemberServiceImpl memberService() {
        return new MemberServiceImpl(memberRepository());
    }

    @Bean
    public  MemoryMemberRepository memberRepository() {
        return new MemoryMemberRepository();
    }

    @Bean
    public OrderServiceImpl orderService() {
        return new OrderServiceImpl(memberRepository(), discountRepository());
    }

    @Bean
    public FixDiscountPolicy discountRepository() {
        return new FixDiscountPolicy();
    }
}


