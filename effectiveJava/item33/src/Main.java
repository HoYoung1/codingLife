// 우리가 여태까지 다뤘던 제네릭에서는 매개변수화 하는 대상은 컨테이너 자체였다
//public class Favorite<T> {
//
//}

//Favorite<String> names = new Favorite<>();
//Favorite<Integer> numbers = new Favorite<>();

public class Main {
    public static void main(String[] args) {


        Favorites f = new Favorites();
        f.putFavorite((Class)String.class, 1);
        f.putFavorite(Integer.class, 1);
        f.putFavorite(Class.class, Favorites.class);
        String favoriteString = f.getFavorite (String.class);
        int favoritelnteger = f.getFavorite(Integer.class);
        Class<?> favoriteClass = f.getFavorite(Class.class);
        System.out.printf("%s %x %s%n", favoriteString, favoritelnteger, favoriteClass.getName());
    }

}
