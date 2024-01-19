package class1.ex;

public class MovieReviewMain2 {
    public static void main(String[] args) {
        MovieReview inception = new MovieReview();
        inception.title = "인셉션";
        inception.review = "인생은 무한루프";

        MovieReview aboutTime = new MovieReview();
        aboutTime.title = "어바웃 타임";
        aboutTime.review = "인생 시간 영화";

        MovieReview movieReview[] = {inception, aboutTime};

        for (MovieReview review : movieReview) {
            System.out.println("영화 제목 : " + review.title + " review : " + review.review);

        }

//        System.out.println("영화 제목 : " + inception.title + " review : " + inception.review);
//        System.out.println("영화 제목 : " + aboutTime.title + " review : " + aboutTime.review);



    }
}
