import java.io.File;


public class FileDeleting{
    public static void main(String[] args) {
        File f = new File("sample.txt");
        if(f.delete()){
            System.out.println("File Deleted Successfully");
        }
        else{
            System.out.println("Unable to delete file");
        }
    }
}
