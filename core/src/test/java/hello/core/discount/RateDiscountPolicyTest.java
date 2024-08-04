package hello.core.discount;

import hello.core.member.Grade;
import hello.core.member.Member;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class RateDiscountPolicyTest {

    @Test
    @DisplayName("VIP는 10% 할인 되어야 한다. ")
    public void vip_o() {
        // given
        Member member = new Member(1L, "hy", Grade.VIP);
        DiscountPolicy discountPolicy = new RateDiscountPolicy();

        // when
        int discountPrice = discountPolicy.discount(member, 10000);

        // then
//        assertEquals(discountPrice, 1000);
        Assertions.assertThat(discountPrice).isEqualTo(1000);
    }

    @Test
    @DisplayName("VIP가 아니면 할인이 적용되지 않아야한다.")
    public void vip_x() {
        // given
        Member member = new Member(2L, "hy", Grade.BASIC);
        DiscountPolicy discountPolicy = new RateDiscountPolicy();

        // when
        int discountPrice = discountPolicy.discount(member, 10000);

        // then
//        assertEquals(discountPrice, 1000);
        Assertions.assertThat(discountPrice).isEqualTo(0);
    }
}