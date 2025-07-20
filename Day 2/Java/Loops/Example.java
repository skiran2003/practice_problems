package Loops;

public class Example {
	public static void main(String[] args) {
		int num=5;
		do {
			num++;
			System.out.println(num);  // do-while loop
		}
		while (num<5);
		
		for(int i=2;i<10;i+=2) {
			System.out.println(i);   // for loop
		}
	}
}
