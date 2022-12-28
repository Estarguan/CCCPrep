import java.util.*;

public class testing {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt(), m = s.nextInt(), x = s.nextInt();
        if (x < n * m) {
            System.out.println(":blobsob:\n" + (n * m - x));
        } else {
            System.out.println(":poggies:");
        }
    }
}