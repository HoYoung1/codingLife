package chapter7initString.chapter7;

public class Instagram {
    // 사진 관련 데이터를 HTML로 내보내는 코드를 준비했다.
    public String renderPerson(OutStream outStream, Person person) {
        String result = "";
        result += "<p>" + person.name + "</p>" + "\n";
        result += renderPhoto(person.photo) + "\n";
        result += "<p>제목: " + person.photo.title + "</p>" + "\n";
        result += emitPhotoData(person.photo) + "\n";
        return result;
    }

    public String photoDiv(Photo p) {
        String result = "";
        result += "<div>" + "\n";
        result += "<p>제목: " + p.title + "</p>" + "\n"; // 제목 출력
        result += emitPhotoData(p) + "\n";
        result += "</div>" + "\n";
        return result;
    }

    private String renderPhoto(Photo photo) {
        return "<p>인스타그램 사진 렌더링~</p>";
    }

    private String emitPhotoData(Photo aPhoto) {
        String result = "";
        result += ("<p>위치: " + aPhoto.location + "</p>") + "\n";
        result += ("<p>날짜: " + aPhoto.date.toString() + "</p>") + "\n";
        return result;
    }


}
