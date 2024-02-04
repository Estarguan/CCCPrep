import java.util.*;
import java.io.*;

public class q4 {
  static int n; static List<Integer> adj1[],adj2[];
  static List<int []> ans;
  public static void main(String[] args) throws IOException{
    Scanner scan = new Scanner(System.in);
    n = scan.nextInt();
    adj1 = new ArrayList[n+1];
    adj2 = new ArrayList[n+1]; ans = new ArrayList<>();
    for (int i = 0; i <= n; ++i){
      adj1[i] = new ArrayList<>(); adj2[i] = new ArrayList<>();
    }
    for (int i = 1; i < n; i++){
      int u = scan.nextInt(), v = scan.nextInt();
      adj1[u].add(v); adj1[v].add(u);
    }
    System.out.println(1 + adj1[1].size());
    dfs(1,0,adj1,true); dfs(1,0,adj2,false); print();
    for (int u : adj1[1]){dfs(u,0,adj2,false); print();}
  }
  static void dfs(int u ,int pre, List<Integer> adj[], boolean f){
    for (int v : adj[u]){
      if (v==pre)continue;
      if (f) adj2[pre].add(v);
      else ans.add(new int[] {u,v});
      dfs(v,u,adj,f);
    }
  }
  static void print(){
    System.out.println(ans.size()+1);
    for (int e[]:ans) System.out.println(e[0]+ " "+ e[1]);
    ans.clear();
  }
}
