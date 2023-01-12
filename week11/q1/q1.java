import java.util.*;

public class q1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int lim = input.nextInt();
        int speed = input.nextInt();
        if (speed>lim){
        	int x;
            if (speed-lim <= 20){
                 x = 100;
            }else if (21 < speed-lim && speed-lim <= 30){
                 x = 270;
            }else{
                 x = 500;
            }
            System.out.println("You are speeding and your fine is $" + x + ".");
        }else{
            System.out.println("Congratulations, you are within the speed limit!");
        }
        input.close();
    }
}
