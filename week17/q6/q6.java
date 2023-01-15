import java.util.*;
public class q6 {
  public static void main(String[] args){
    Scanner s = new Scanner(System.in);
    int t = s.nextInt();
    int[] cows = new int[t];
    for (int i = 0; i < t; ++i){
      cows[i] = s.nextInt();
    }
    Arrays.sort(cows);
    int ans = 0, tuition = 0;
    for (int i=0; i < t; ++i){
      int fee=cows[i];
      int money = (t-i) * fee;
      if (money>ans){
        ans = money;
        tuition = fee;
      }

    }
    System.out.print(ans + " " + tuition);
  }


}
