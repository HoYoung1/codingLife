package chapter7sout;


public class FaceBook {
    public static void main(String[] args) {
        // 변수 준비
        Photo hoYeongPhoto = new Photo();
        Person hoYeong = new Person("HoYeong", hoYeongPhoto);

        // renderPerson 사용
        new Instagram().renderPerson(new OutStream(), hoYeong);

        System.out.println("\n");

        // photoDiv 사용
        new Instagram().photoDiv(hoYeongPhoto);
    }
}
