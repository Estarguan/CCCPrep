import java.util.*;

public class testing{
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    String text = scan.next();
    String s = scan.next();
    ArrayList<String> cyclic = new ArrayList<String>();
    for (int i = 0; i < s.length(); ++i){
      cyclic.add(s);
      s = s.substring(1) + s.charAt(0);
    }
    for (String i : cyclic){
      if (text.contains(i)){
        System.out.println("yes");
        System.exit(0);
      }
    }
    System.out.println("no");
  }
}
