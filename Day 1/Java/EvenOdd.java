package sample;
import java.util.Scanner;
public class EvenOdd {
	public static void main (String args[]) {
		Scanner s = new Scanner(System.in);
		System.out.println("Enter a number: ");
		int num = s.nextInt();
		if(num%2==0) {
			System.out.println("Even");
		}
		else if(num==0) {
			System.out.println("Zero");
		}
		else {
			System.out.println("Odd");
		}
	}
}
