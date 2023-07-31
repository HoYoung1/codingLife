import java.io.*;

public class AdapterExample {
    public static void main(String[] args) {
        try {
            InputStream is = new FileInputStream("./numbers.txt");
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(is));
            System.out.println(bufferedReader.readLine());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }


}
