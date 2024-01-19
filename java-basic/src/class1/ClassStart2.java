package class1;

public class ClassStart2 {
    public static void main(String[] args) {
        String[] studentNames = {"학생1", "학생2"};
        int[] studentAges = {15, 16};
        int[] studentGrades = {90, 80};

//        String student1Name = "학생1";
//        int student1Age = 15;
//        int student1Grade = 90;
//
//        String student2Name = "학생2";
//        int student2Age = 16;
//        int student2Grade = 80;

        for (int i = 0; i < studentNames.length; i++) {
            System.out.println("이름: " + studentNames[i] + " 나이: " + studentAges[i] + " 성적: " + studentGrades[i]);

        }

//        System.out.println("이름: " + student1Name + " 나이: " + student1Age + " 성적: " + student1Grade);
//        System.out.println("이름: " + student2Name + " 나이: " + student2Age + " 성적: " + student2Grade);

    }
}
