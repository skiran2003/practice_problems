package sample;
import java.util.Scanner;
public class LargestNumber {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		System.out.println("Enter three numbers: ");
		int n1=s.nextInt();
		int n2=s.nextInt();
		int n3=s.nextInt();
		if(n1>n2) {
			if(n2>n3) {
				System.out.println(n1+" is the largest");
			}
			else if(n3>n1) {
				System.out.println(n3+" is the largest");
			}
		}
		else if(n2>n3){
			System.out.println(n2+" is the largest");
		}
		else {
			System.out.println(n3+" is the largest");
		}
	}
}
