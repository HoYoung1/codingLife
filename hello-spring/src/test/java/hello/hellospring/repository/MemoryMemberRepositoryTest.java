package hello.hellospring.repository;

import hello.hellospring.domain.Member;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.springframework.util.Assert;

import java.util.List;
import java.util.Optional;

import static org.assertj.core.api.Assertions.*;

class MemoryMemberRepositoryTest {

    MemoryMemberRepository repository = new MemoryMemberRepository();

    @AfterEach
    public void afterEach() {
        repository.clearStore();
    }

    @Test
    void save() {
        Member member = new Member();
        String testName = "hy";
        member.setName(testName);
        repository.save(member);

//        Member save = repository.save(member);
//        assert save.getName().equals(testName);

        Member result = repository.findById(member.getId()).get();
        Assertions.assertEquals(member, result);

        assertThat(member).isEqualTo(result);
    }

    @Test
    void findById() {
        Member member = new Member();
        String testName = "findById";
        member.setName(testName);
        Member save = repository.save(member);

        Optional<Member> byId = repository.findById(1L);
//        byId.ifPresent(assert member1 -> member1.getName().equals(testName));
        assert save.getName().equals(testName);
    }

    @Test
    void findByName() {
        Member member1 = new Member();
        member1.setName("spring1");
        repository.save(member1);

        Member member2 = new Member();
        member2.setName("spring2");
        repository.save(member2);


        assertThat(member1).isEqualTo(repository.findByName("spring1").get());
    }

    @Test
    void findAll() {
        Member member1 = new Member();
        member1.setName("spring1");
        repository.save(member1);

        Member member2 = new Member();
        member2.setName("spring2");
        repository.save(member2);

        List<Member> result = repository.findAll();
        assertThat(result.size()).isEqualTo(2);
        assertThat(result).contains(member1, member2);
    }
}