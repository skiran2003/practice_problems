import java.io.FileWriter;
import java.io.IOException;
public class FileWriting{
    public static void main(String[] args) {
        try {
            FileWriter w = new FileWriter("sample.txt");
            w.write("We are performing FileWrite operation");
        } catch (IOException e) {
            System.out.println("Error occured");
        }

    }
}