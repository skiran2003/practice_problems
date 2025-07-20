import java.util.Scanner;

public class Divisibility {
	public static void main (String[] args) {
		Scanner s = new Scanner(System.in);
		System.out.println("Enter a number: ");
		int num = s.nextInt();
		if(num%3==0 && num%5==0) {
			System.out.println("Divisible by 3 and 5");
		}
		else {
			System.out.println("Not divisible by 3 and 5");
		}
	}
}
