package inclass_practice;
import java.util.*;
public class inclass_practice{
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int k = input.nextInt(), n = input.nextInt();
		int ranks[][] = new int[n][n];
		int ans[][] = new int[n][n];
		int finans = 0;
		for (int i = 0; i < k; ++i) {
			for (int j = 0; j<n; ++j) {
				ranks[i][j] = input.nextInt();
			}
		}

		for (int[] i : ans) {
			Arrays.fill(i, 0);
		}

		for (int x = 0; x < k; ++x) {
			for (int y = 0; y < n; ++y) {
				for (int z = y+1; z < n; ++z) {
					int temp = ranks[x][y];

					ans[temp-1][ranks[x][z]-1]++;
				}
			}
		}


		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (ans[i][j] == k) {
					finans++;
				}
			}
		}
		System.out.println(finans);
	}
}
