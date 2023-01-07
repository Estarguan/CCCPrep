import java.util.*;

public class testing {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int x = s.nextInt(), y = s.nextInt(), n = s.nextInt();
        char grid[][] = new char[y][x];
        for (char[] row : grid) {
            Arrays.fill(row, '.');
        }
        for (int i = 0; i < n; ++i) {
            int x1 = s.nextInt(), y1 = s.nextInt(), x2 = s.nextInt(), y2 = s.nextInt();
            for (int j = y1 - 1; j < y2; ++j) {
                for (int k = x1 - 1; k < x2; ++k) {
                    grid[j][k] = 'X';
                }
            }
        }
        int ans = 0;
        for (char[] row : grid) {
            for (char letter : row) {
                if (letter == 'X') {
                    ans++;
                }
            }
        }
        System.out.println(ans);
    }
}
