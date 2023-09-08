import java.util.*;

public class q1{


  public static boolean is_prime(int num){
    if (num<2){
      return false;
    }for (int i = 2; i < Math.pow(num,0.5)+1; ++i){
      if (num % i == 0){
        return false;
      }
    }
    return true;
  }

  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    int n = scan.nextInt();
    if (is_prime(n)){
      System.out.println("prime");
    }else{
      System.out.println("not");
    }
  }
}