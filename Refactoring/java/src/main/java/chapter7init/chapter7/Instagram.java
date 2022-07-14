package chapter7init.chapter7;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Instagram {
    // 사진 관련 데이터를 HTML로 내보내는 코드를 준비했다.
    public String renderPerson(OutStream outStream, Person person) {
        List<String> result = new ArrayList<>();
        result.add("<p>" + person.name + "</p>");
        result.add(renderPhoto(person.photo));
        result.add("<p>제목: " + person.photo.title + "</p>");
        result.add(emitPhotoData(person.photo));
        return String.join("\n", result);
    }

    public String photoDiv(Photo p) {
        return String.join("\n",
                Arrays.asList(
                        "<div>",
                        "<p>제목: " + p.title + "</p>", // 제목 출력
                        emitPhotoData(p),
                        "</div>"
                ));
    }

    private String renderPhoto(Photo photo) {
        return "<p>인스타그램 사진 렌더링~</p>";
    }

    private String emitPhotoData(Photo aPhoto) {
        List<String> result = new ArrayList<>();
        result.add("<p>위치: " + aPhoto.location + "</p>");
        result.add("<p>날짜: " + aPhoto.date.toString() + "</p>");
        return String.join("\n", result);
    }


}
