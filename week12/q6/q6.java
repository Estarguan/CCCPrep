import java.util.*;

public class q6{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    int n = input.nextInt(), m = input.nextInt();
    List<ArrayList<Integer>> lst = new ArrayList<>();
    for (int i = 0; i <= n;++i){
      lst.add(new ArrayList<>());
    }
    for (int i = 0; i < m; ++i){
      int a = input.nextInt(), b = input.nextInt();
      if (a>b) lst.get(a).add(b);
      else lst.get(b).add(a);
    }
    int ans[] = new int[n+1];
    for (int i = 1; i <= n; ++i){
      for (int k =1; k <= 4; k++){
        boolean work = true;
        for (int x : lst.get(i)){
          if(ans[x]==k) work = false;
        }
        if (work){
          ans[i] = k; break;
        }
      }
    }
    for (int i = 1; i <= n; ++i){
      System.out.print(ans[i]);
    }
  }
}
