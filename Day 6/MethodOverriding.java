package oopspractice;

class Greet{
	void message(){
		System.out.println("Hello");
	}
}

class Greet1{
	void message() {
		System.out.println("Hi");
	}
}
public class MethodOverriding {
	public static void main(String[] args) {
		Greet g =new Greet();
		Greet1 g1=new Greet1();
		g.message();
		g1.message();
	}
}
