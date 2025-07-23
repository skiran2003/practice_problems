import java.io.File;
import java.io.IOException;

public class CreateFile{
    public static void main(String[] args) throws IOException{
        File newFile = new File("sample.txt");
            if(newFile.createNewFile()){
                System.out.println("File created successfully:");
            }
            else{
                System.out.println("File already exists");
            }

    }
}