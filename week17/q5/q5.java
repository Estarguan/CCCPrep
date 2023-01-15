import java.io.*;
import java.util.*;

public class q5 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        String lin1 = s.next();
        String lin2 = s.next();
        int count = 0;
        for (int i = 0; i < n; ++i){
            if (lin1.charAt(i) == 'S' && lin2.charAt(i) == 'S'){
                count++;
            }
        }
        System.out.println((count > 2)?"NO":"YES");
    }
}