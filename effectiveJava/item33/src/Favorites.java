import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

//즐겨찾기를 추가하거나 조회
// 이종 컨테이너 예시
public class Favorites {

    private Map<Class<?>, Object> favorites = new HashMap<>();

    public <T> void putFavorite(Class<T> type, T instance){
//        favorites.put(type, instance);
//        favorites.put(Objects.requireNonNull(type), instance);
        favorites.put(Objects.requireNonNull(type), type.cast(instance));
    }

    @SuppressWarnings("unchecked")
    public <T> T getFavorite(Class<T> type) {
//        return (T) favorites.get(type);
        return type.cast(favorites.get(type));
    }

}
