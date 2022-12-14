import java.util.*;
public class q2{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int count = 0;
        int n = s.nextInt();
        for (int i = 0; i < n; ++i){
            int m = s.nextInt(), o = s.nextInt();
            if (m > o){
                count++;
            }
        }
        System.out.println(count);
    }
}