package abstractionandencapsulation;

class Human{
	private int age=22;
	private String name="Sai";

public int getAge() {
	return this.age;
}
public String getName() {
	return this.name;
}
public void setAge(int age) {
	this.age=age;
}
public void setName(String name) {
	this.name = name;
}
}
public class Encapsulation {
	public static void main(String[] args) {
		Human h = new Human();
		System.out.println("My name is "+h.getName()+" I am "+h.getAge()+" years old.");
	}
}
