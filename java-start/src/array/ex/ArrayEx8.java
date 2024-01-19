package array.ex;

import java.util.Scanner;

public class ArrayEx8 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("학생수를 입력하세요 : ");
        int studentCount = scanner.nextInt();
        int[][] scores = new int[studentCount][3];
        String[] subjects = {"국어", "수학", "영어"};

//        for (int i = 0; i < scores.length; i++) {
//            System.out.println((i+1) + "번 학생의 성적을 입력하세요: ");
//            System.out.print("국어 : ");
//            scores[i][0] = scanner.nextInt();
//            System.out.print("영어 : ");
//            scores[i][1] = scanner.nextInt();
//            System.out.print("수학 : ");
//            scores[i][2] = scanner.nextInt();
//        }
        for (int i = 0; i < studentCount; i++) {
            System.out.println((i+1) + "번 학생의 성적을 입력하세요: ");
            for (int j = 0; j < subjects.length; j++) {
                System.out.print(subjects[j] + " : ");
                scores[i][j] = scanner.nextInt();
            }
        }

        for (int i = 0; i < studentCount; i++) {
            int total = 0;
            for (int j = 0; j < scores[i].length; j++) {
                total += scores[i][j];
            }
            System.out.println((i+1)+"학생의 총점:"+ total+", 평균:" + (double)total/scores[i].length);
        }
    }
}
