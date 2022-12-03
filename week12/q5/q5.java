import java.util.Scanner;
import java.util.HashMap;
import java.util.Map;
public class randomTesting{
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
		for (int[] z : ranks) {
			System.out.println(z);
		}

	}
}