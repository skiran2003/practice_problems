package oopspractice;

class Animal{
	void cry() {
		System.out.println("Crying....");
	}
}
class Dog extends Animal{
	void cry() {
		System.out.println("Barking....");
	}
}

public class InheritanceExample {
	public static void main(String[] args) {
		Dog d = new Dog();
		d.cry();
	}

}
