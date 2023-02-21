import java.util.*;

// the codes too slow but it works so yea

public class testing {
    public static void main(String[] args) {
        Scanner Scanner = new Scanner(System.in);
        int t = Scanner.nextInt();
        for (int z = 0; z < t; ++z) {
            String s = Scanner.next();
            for (int i = 0; i < s.length() - 1; ++i) {
                if (s.charAt(i) == s.charAt(i + 1)) {
                    s = s.replaceFirst(String.valueOf(s.charAt(i)), ".");
                }
            }
            int count = 0;
            for (int i = 0; i < s.length();++i){
                if (s.charAt(i) == 'A' || s.charAt(i) == 'B'){
                    count++;
                }
            }
            System.out.println(s.length()-count);
        }
    }
}