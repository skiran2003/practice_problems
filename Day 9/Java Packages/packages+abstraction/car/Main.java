package car;
import vehicle.Vehicle;
import engine.Engine;

class Car extends Engine implements Vehicle{
    @Override
    public void start(){
        System.out.println("Car started...");
    }
    @Override
    public void FuelType(){
        System.out.println("Diesel engine");
    }
}

public class Main{
    public static void main(String[] args) {
        Car c = new Car();
        c.start();
        c.FuelType();
    }
}
