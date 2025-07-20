package methods;

public class VarargsExample {
	void printNumbers(int...nums) {
		for(int num:nums) {
			System.out.println(num);
		}
	}
	public static void main(String[] args) {
		VarargsExample va=new VarargsExample();
		va.printNumbers(1,2,3,4,5,6,7);
	}
}
