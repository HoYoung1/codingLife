package hello.hellospring;

import hello.hellospring.repository.*;
import hello.hellospring.service.MemberService;
import jakarta.persistence.EntityManager;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import javax.sql.DataSource;

@Configuration
public class SpringConfig {

    private final DataSource dataSource;
    private final EntityManager entityManager;

    private final MemberRepository memberRepository;

    public SpringConfig(DataSource dataSource, EntityManager entityManager, SpringDataJpaMemberRepository memberRepository1) {
        this.dataSource = dataSource;
        this.entityManager = entityManager;
        this.memberRepository = memberRepository1;
    }

    @Bean
    public MemberService memberService() {
        return new MemberService(memberRepository());
    }

    @Bean
    public MemberRepository memberRepository() {
//        return new MemoryMemberRepository();
//        return new JdbcMemberRepository(dataSource);
//        return new JdbcTemplateMemberRepository(dataSource);
//        return new JpaMemberRepository(entityManager);
        return memberRepository;
    }

}
