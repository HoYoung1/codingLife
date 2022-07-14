package chapter7;

public class Instagram {
    // 사진 관련 데이터를 HTML로 내보내는 코드를 준비했다.
    public void renderPerson(OutStream outStream, Person person) {
        System.out.println("<p>" + person.name + "</p>");
        renderPhoto(person.photo);
        emitPhotoData(person.photo);
        System.out.println("<p>날짜: " + person.photo.date.toString() + "</p>");
    }

    public void photoDiv(Photo p) {
        System.out.println("<div>");
        emitPhotoData(p);
        System.out.println("<p>날짜: " + p.date.toString() + "</p>");
        System.out.println("</div>");
    }

    private void emitPhotoData(Photo p) {
        System.out.println("<p>제목: " + p.title + "</p>");
        System.out.println("<p>위치: " + p.location + "</p>");
    }

    private void renderPhoto(Photo photo) {
        System.out.println("<p>인스타그램 사진 렌더링~</p>");
    }


}
