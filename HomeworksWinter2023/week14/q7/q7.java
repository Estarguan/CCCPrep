import java.util.Scanner;
public class q7 {
  static String base = "Good writing is good writing is good writing.";
  static String pre = "Good writing is good ";
  static String mid = " writing is good ";
  static String suf = " is good writing.";

  static long len[] = new long[31];
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    len[0] = base.length();
    for (int i = 1; i < len.length; i++){
      len[i] = pre.length() + len[i-1] + mid.length() + len[i-1] + suf.length();
    }
    int q = scan.nextInt();
    for (int i = 0; i < q; i++ ){
      int n = scan.nextInt(), k = scan.nextInt();
      System.out.println(k > len[n]? '.' : fun(n,k-1));
    }
    scan.close();
  }

  static char fun(int lvl, int idx){
    if (lvl == 0){
      return base.charAt(idx);
    }
    if (idx < pre.length()) {
      return pre.charAt(idx);
    }
    idx -= pre.length();
    if (idx < len[lvl-1]) return fun(lvl-1,idx);
    idx -= len[lvl-1];
    if (idx < mid.length()){
      return mid.charAt(idx);
    }
    idx -= mid.length();
    if (idx < len[lvl-1]) return fun(lvl-1,idx);
    idx -= len[lvl-1];
    
    return suf.charAt(idx);
  }
}
