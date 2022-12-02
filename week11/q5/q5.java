import java.util.*;

public class q5{
  public static void main(String[] args){
    Scanner input = new Scanner(System.in);
    int n = input.nextInt();
    Deque<Integer> a = new LinkedList<>();
    for (int i = 0; i < n; i++){
      a.add(input.nextInt());
    }
    int ans = 0;
    while (a.size() > 1){
      if (a.peekFirst().equals(a.peekLast())) {
          a.pollFirst();
          a.pollLast();
      } else if (a.peekFirst() > a.peekLast()) {
          ans++;
          a.addLast(a.pollLast() + a.pollLast());
      } else {
          ans++;
          a.addFirst(a.pollFirst() + a.pollFirst());
      }
    }
    System.out.println(ans);
  }
}
