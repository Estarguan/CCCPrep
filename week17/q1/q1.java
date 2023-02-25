import java.util.*;

public class q1 {
  public static void main(String[] args){
    Scanner s = new Scanner(System.in);
    int max = s.nextInt();
    int A = s.nextInt(), B = s.nextInt(), C = s.nextInt();
    if (A+B*4+C*7 <= max){
      System.out.println("Time to go shopping!");
    }else{
      System.out.println("You cannot afford them all.");
    }
  }
}
