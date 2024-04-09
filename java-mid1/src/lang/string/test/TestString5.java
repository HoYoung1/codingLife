package lang.string.test;

public class TestString5 {
    public static void main(String[] args) {
        String fileName = "hello.txt";
        String ext = ".txt";

        System.out.println("filename : " + fileName.substring(0,fileName.indexOf(ext)));
        System.out.println(ext);
    }

}
