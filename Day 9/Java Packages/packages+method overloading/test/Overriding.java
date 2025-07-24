package test;
import animal.Animal;

class Dog extends Animal{
    public Dog(){
        
    }
    public Dog(String breed){
        super(breed);
    }
    @Override
    public void makeSound(){
        System.out.println("Barking...");

        
    }
}
class Puppy extends Dog{
    @Override
    public void makeSound(){
        System.out.println("Weeping...");
    }
}

public class Overriding{
    public static void main(String[] args) {
        Dog g = new Dog("Bulldog");
        g.makeSound();
        Puppy p = new Puppy();
        p.makeSound();
    }
}