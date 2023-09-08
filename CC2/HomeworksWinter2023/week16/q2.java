import java.util.*;

public class q2 {
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    int x = scan.nextInt(), y = (int)Math.sqrt(x);
    for (int i = 2; i <= y; i++){
      System.out.println(i);
      while (x%i == 0){
        System.out.println(i + " "); x/= i;
      }
    }
    if (x!=1) System.out.println(x);
    else System.out.println();
  }
}
