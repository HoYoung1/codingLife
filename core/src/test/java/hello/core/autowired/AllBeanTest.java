package hello.core.autowired;

import hello.core.AutoAppConfig;
import hello.core.discount.DiscountPolicy;
import hello.core.member.Grade;
import hello.core.member.Member;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import java.util.List;
import java.util.Map;

public class AllBeanTest {
    @Test
    void findAllBean() {
        AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AutoAppConfig.class, DiscountService.class);
        DiscountService discountService = ac.getBean(DiscountService.class);

        Member vipMember = new Member(1L, "vip", Grade.VIP);

        int actual = discountService.discount(vipMember, 10000, "fixDiscountPolicy");
        Assertions.assertThat(actual).isEqualTo(1000);

        int actual2 = discountService.discount(vipMember, 20000, "rateDiscountPolicy");
        Assertions.assertThat(actual2).isEqualTo(2000);

    }

    static class DiscountService {
        private Map<String, DiscountPolicy> discountPolicyMap;
        private List<DiscountPolicy> discountPolicyList;

        @Autowired
        public DiscountService(Map<String, DiscountPolicy> discountPolicyMap, List<DiscountPolicy> discountPolicyList) {
            this.discountPolicyMap = discountPolicyMap;
            this.discountPolicyList = discountPolicyList;
            System.out.println("discountPolicyMap = " + discountPolicyMap);
            System.out.println("discountPolicyList = " + discountPolicyList);
        }

        public int discount(Member member, int price, String discountCode) {
            DiscountPolicy discountPolicy = discountPolicyMap.get(discountCode);
            return discountPolicy.discount(member, price);
        }
    }
}
