package hello.core.singletone;

public class SingletonService {

    private static final SingletonService instance = new SingletonService();

    public static SingletonService getInstance() {
        return instance;
    }

    // 객체 생성 못함
    private SingletonService() {

    }
}
