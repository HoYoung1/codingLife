package array;

public class Array1Ref4 {
    public static void main(String[] args) {
        int[] students = {90, 80, 70, 60, 50}; // 배열 생성과 초기화

        //변수 값 대입
//        students[0] = 90;
//        students[1] = 80;
//        students[2] = 70;
//        students[3] = 60;
//        students[4] = 50;

        for (int i = 0; i < students.length; i++) {
            System.out.println("student[" + (i+1)  + "] " + students[i]);
        }
    }
}
