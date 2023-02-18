import java.util.Scanner;
public class Main{
  public static void main(String[] args){
    Scanner s = new Scanner(System.in);
    int n = s.nextInt();
    int t1[] = new int[n];
    int t2[] = new int[n];
    for (int i = 0; i < n; ++i){
      t1[i] = s.nextInt();
    }
    for (int i = 0; i < n; ++i){
      t2[i] = s.nextInt();
    }
    int c1=0,c2=0,ans=0;
    for (int i = 0; i < n; ++i){
      c1 += t1[i];
      c2 += t2[i];
      if (c1==c2){
        ans = i+1;
      }
    }
    System.out.println(ans);
  }
}