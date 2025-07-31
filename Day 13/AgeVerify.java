// Creating Custom Exception which extends the Exception super class

class UnderAgeException extends Exception{
    public UnderAgeException(String s){
        super(s); // Passes the string to parent Exception class
    }
}

public class AgeVerify{
    public void verifyAge(int age){
        try {
            if(age<18){
            throw new UnderAgeException("You must be 18 or older"); 
            }
            else{
                System.out.println("You are above 18 years");
            }
        } catch (UnderAgeException e) {  // Catching the custom exception we created
            System.out.println(e);
        }
    }

    public static void main(String[] args){
        int age=16;
        AgeVerify av = new AgeVerify();
        av.verifyAge(age);
    }
}