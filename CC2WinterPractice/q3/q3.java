import java.util.*;

public class q3 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        String a = s.next();
        String b = s.next();
        int maxcnt = 0;
        if (b.length() >= a.length()) {
            int cnt = 0;
            for (int i = 0; i < b.length(); ++i) {
                for (int j = i + 1; j < b.length() + 1; ++j) {
                    // System.out.println(b.substring(i, j));
                    if (a.startsWith(b.substring(i, j))) {
                        cnt = j - i;
                        if (cnt > maxcnt) {
                            maxcnt = cnt;
                        }
                    } else if (a.endsWith(b.substring(i, j))) {
                        cnt = j - i;
                        if (cnt > maxcnt) {
                            maxcnt = cnt;
                        }
                    }
                }
            }
        } else {
            int cnt = 0;
            for (int i = 0; i < a.length(); ++i) {
                for (int j = i + 1; j < a.length() + 1; ++j) {
                    if (b.startsWith(a.substring(i, j))) {
                        cnt = j - i;
                        if (cnt > maxcnt) {
                            maxcnt = cnt;
                        }
                    } else if (b.endsWith(a.substring(i, j))) {
                        cnt = j - i;
                        if (cnt > maxcnt) {
                            maxcnt = cnt;
                        }
                    }
                }
            }
        }
        System.out.println(maxcnt);
    }
}
