package abstractionandencapsulation;
abstract class Shape{
	abstract double perimeter();
	abstract double area();
}
class Circle extends Shape{
	int radius;
	Circle(int radius){
		this.radius=radius;
	}
	double perimeter() {
		return 2*3.14*radius;
	}
	double area() {
		return 3.14*radius*radius;
	}
}
class Rectangle extends Shape{
	int length;
	int breadth;
	double perimeter() {
		return 2*(length+breadth);
	}
	double area() {
		return length*breadth;
	}
}

public class Abstraction {
	public static void main(String[] args) {
		Circle c=new Circle(5);
		System.out.println(c.area());
	}
}
