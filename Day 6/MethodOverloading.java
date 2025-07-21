package oopspractice;


class Rectangle{
	int area(int length,int breadth) {
		return length * breadth;
	}
}

class Circle{
	double area(int radius) {
		return 3.14*radius*radius;
	}
}

public class MethodOverloading {
	public static void main(String[] args) {
		int length=9;
		int breadth=15;
		int radius=5;
		Rectangle r = new Rectangle();
		Circle c = new Circle();
		System.out.println(c.area(radius));
		System.out.println(r.area(length, breadth));
	}
}
