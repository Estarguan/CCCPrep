import java.util.*;
public class q7 {
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    int n = input.nextInt(), a[] = new int[n];
    for (int i = 0; i < n; ++i){
      a[i] = input.nextInt();
    }
    int ans = 0;
    for (int i = 0; i < n; ++i){
      int sum = 0;
      for (int j = i; j <n; j++){
        sum += a[j];
        for (int k = i; k <= j; ++k){
          if (a[k] * (j-i+1) == sum){
            ans++; break;
          }
        }
      }
    }
    System.out.println(ans);
  }
}
