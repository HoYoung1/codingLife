package hello.core.member;

import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.Test;

public class MemberServiceTest {

    @Test
    void join() {
        //given
        Member member = new Member(1L, "memberA", Grade.VIP);
        MemberService memberService = new MemberServiceImpl();

        //when
        memberService.join(member);
        Member findmember = memberService.findMember(member.getId());

        //then
        Assertions.assertThat(member).isEqualTo(findmember);
        Assertions.assertThat(member.getName()).isEqualTo("memberA");
    }
}
