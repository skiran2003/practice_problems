package oopspractice;

class Shape{
	void dimension(){
		System.out.println("Quadrilateral");
	}
}

class Square extends Shape{
	void area(int side) {
		System.out.println("Area of square is: " + side*side);
	}
}

class Cube extends Square{
	void volume(int side) {
		System.out.println("Volume of cube is: " + side*side*side);
	}
}
public class MultilevelInheritance {
	public static void main(String[] args) {
		Cube c = new Cube();
			c.volume(8);
			c.area(6);
			c.dimension();
	}
}
