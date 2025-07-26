import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class RegexExample{
    public static void main(String[] args) {
        Pattern p = Pattern.compile("Java",Pattern.CASE_INSENSITIVE);
        Matcher m =p.matcher("Java Regular Expressions..");
        boolean match = m.find();
        System.out.println(match);
    }}
