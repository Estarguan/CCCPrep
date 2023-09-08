import java.util.*;

public class q5{
  public static void main(String[] args){
    Scanner s = new Scanner(System.in);
    int n = s.nextInt();
    int target = s.nextInt();
    int[] h = new int[n+1];
    for (int i = 1; i <=n; i++){
      h[i] = s.nextInt();
    }
    List<Integer> comb = new ArrayList<>();
    getComb(1,n,comb);
    System.out.println(ans);
  }
  static void getComb(int i, int n, List<Integer> comb){
    if (i > n){
      int sum = 0;
      for (int idx:comb){
        sum += h[idx];
      }
      if (sum >= target) {ans = Math.min(ans,sum-target);}
      return;
    }
    getComb(i+1,n,comb);
    comb.add(i); getComb(i+1,n,comb);
    comb.remove(comb.indexOf(-1));
  }
}