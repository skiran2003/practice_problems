// Using Throws keyword to pass the exception to other methods
import java.io.IOException;

public class ThrowsExample{
    public void methodA() throws IOException{
        System.out.println("This is method A:");
        // Throwing an IO Exception which needs to be handled by other methods which call this method
        throw new IOException("IOException occured in method A");

    }
    public void methodB() throws IOException{
        System.out.println("This is method B:");
        ThrowsExample t = new ThrowsExample();
        t.methodA();
        // IO Exception is not handled in this method hence it is passed to methodC
    }
    public void methodC() throws IOException{
        System.out.println("This is method C:");
        ThrowsExample t = new ThrowsExample();
        t.methodB();
        // IO Exception not handled in this method also so it is passed to main method
    }

    public static void main(String[] args) {
        ThrowsExample t = new ThrowsExample();
        try {
            t.methodC();
            // Here we are handling the exception throwed by methodA
        } catch (IOException e) {
            System.out.println(e);
        }
    }
}