import java.util.HashSet;
import java.util.Set;
public class ArithmeticProgression{
    public static Set<Integer> findProgression(int starting,int cd,HashSet<Integer> intSet){
        Set<Integer> newSet = new HashSet<>();
        if(cd==0){
            if(intSet.contains(starting)){
                newSet.add(starting);
            }
        }
        else{
            for(int i:intSet){
                if((i-starting)%cd==0){
                    newSet.add(i);
                }
            }
        }
        return newSet;
}
public static void main(String[] args) {
    HashSet<Integer> intSet= new HashSet<>();
    // intSet.add(5);
    intSet.add(9);
    intSet.add(12);
    intSet.add(7);
    intSet.add(25);
    int starting=5;
    int cd=0;
    Set<Integer> result=findProgression(starting,cd,intSet);
    System.out.println(result);
}
}