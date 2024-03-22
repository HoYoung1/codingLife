package hello.hellospring.repository;

import hello.hellospring.domain.Member;

import java.util.*;

public class MemoryMemberRepository implements MemberRepository{

    private static Map<Long, Member> store = new HashMap<>();
    public static long sequence = 0L;
    @Override
    public Member save(Member member) {
        member.setId(++sequence);
        store.put(member.getId(), member);
        return member;
    }

    @Override
    public Optional<Member> findById(Long id) {
        return Optional.ofNullable(store.get(id));
    }

    @Override
    public Optional<Member> findByName(String name) {
//        for (Long id : store.keySet()) {
//            if (store.get(id) != null) {
//                if (store.get(id).getName().equals(name)) {
//                    return Optional.ofNullable(store.get(id));
//                }
//            }
//        }

        return store.values()
                .stream()
                .filter(x -> x.getName().equals(name))
                .findAny();
    }

    @Override
    public List<Member> findAll() {
//        return store.values().stream().toList();
        return new ArrayList<>(store.values()); //
    }

    public void clearStore() {
        sequence = 0;
        store.clear();
    }
}
