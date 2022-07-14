package chapter7sout;

public class Instagram {
    // 사진 관련 데이터를 HTML로 내보내는 코드를 준비했다.
    public void renderPerson(OutStream outStream, Person person) {
        System.out.println("<p>" + person.name + "</p>");
        renderPhoto(person.photo);
        System.out.println("<p>제목: " + person.photo.title + "</p>");
        emitPhotoData(person.photo);
    }

    public void photoDiv(Photo p) {
        System.out.println("<div>");
        System.out.println("<p>제목: " + p.title + "</p>");
        emitPhotoData(p);
        System.out.println("</div>");
    }

    private void renderPhoto(Photo photo) {
        System.out.println("<p>인스타그램 사진 렌더링~</p>");
    }

    private void emitPhotoData(Photo aPhoto) {
        System.out.println("<p>위치: " + aPhoto.location + "</p>");
        System.out.println("<p>날짜: " + aPhoto.date.toString() + "</p>");
    }


}
