package animal;

public class Animal{
    protected Animal(){
        System.out.println("Animal breed unknown ");
    }
    public Animal(String breed){
        System.out.println("Animal breed is: "+breed);
    }
    protected void makeSound(){
        System.out.println("Making sound");
    }
}