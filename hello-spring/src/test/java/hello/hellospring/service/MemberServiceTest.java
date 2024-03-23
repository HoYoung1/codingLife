package hello.hellospring.service;

import hello.hellospring.domain.Member;
import hello.hellospring.repository.MemoryMemberRepository;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.*;

class MemberServiceTest {

    MemoryMemberRepository repository;
    MemberService memberService;

    @AfterEach
    public void afterEach() {
        repository.clearStore();
    }

    @BeforeEach
    public void beforeEach() {
        repository = new MemoryMemberRepository();
        memberService = new MemberService(repository);
    }


//    @Test
//    void join() {
//        Member member = new Member();
//        member.setName("joinTest");
//        memberService.join(member);
//
//        Member member2 = new Member();
//        member2.setName("joinTest");
//        assertThrows(IllegalArgumentException, memberService.join(member2));
//    }

    @Test
    void 회원가입() {
        // given
        Member member = new Member();
        member.setName("회원가입테스트");

        // when
        memberService.join(member);

        // then
        assertThat(member).isEqualTo(memberService.findMembers().stream().findFirst().get());
    }

    @Test
    void 회원가입2() {
        // given
        Member member = new Member();
        member.setName("회원가입테스트");

        // when
        long memberId = memberService.join(member);

        // then
//        assertThat(memberId).isEqualTo(memberService.findMembers().stream().findFirst().get().getId());
        Member findMember = memberService.findOne(memberId).get();
//        assertThat(member).isEqualTo()
        assertThat(member).isEqualTo(findMember);
    }


    @Test
    void 회원가입_중복회원_예외발생() {
        // given
        Member member1 = new Member();
        member1.setName("중복회원테스트");

        Member member2 = new Member();
        member2.setName("중복회원테스트");

        // when
        memberService.join(member1);


        // then
//        assertThat(memberId).isEqualTo(memberService.findMembers().stream().findFirst().get().getId());
        Assertions.assertThrows(IllegalArgumentException.class, () -> memberService.join(member2));
    }


//    @Test
//    void findMembers() {
//    }
//
//    @Test
//    void findOne() {
//    }
}