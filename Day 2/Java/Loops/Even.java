package Loops;
import java.util.Scanner;

public class Even {
	public String CheckEven(int num) {
		if(num%2==0){
			return"Even";
		}
		return "Odd";
	}
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		System.out.println("Enter a number:");
		int num = s.nextInt();
		Even e=new Even();
		String result = e.CheckEven(num);
		System.out.println(result);
		s.close();
	}
}
