import java.util.regex.Matcher;
import java.util.regex.Pattern;


public class PasswordChecking{
    public static void main(String[] args){
    String pattern = "^(?=.*[\\w])+(?=.*[!@#$%^&*()_\\-]).{8,}$";
    Pattern p =Pattern.compile(pattern);
    Matcher m = p.matcher("Sai@1701");
    boolean valid=m.find();

    if(valid){
        System.out.println("Password Accepted");
    }
    else{
        System.out.println("Invalid Password Format");
    }
}
}