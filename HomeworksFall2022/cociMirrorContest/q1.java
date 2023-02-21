import java.util.Scanner;
public class inclass_practice {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int n = input.nextInt(), r = input.nextInt(), s = input.nextInt();
		for (int x = 0; x < n; ++x) {
			int max = -1, min = r+1;
			String mat[] = new String[r];
			for (int y = 0; y < r; ++y) {
				mat[y] = input.next();
			}
			for (int i = 0; i < s; ++i) {
				for (int j = 0; j < r; ++j) {
					if (mat[j].charAt(i) == '#') {
						if (j+1 > max) {
							max = j+1;
						}
						if (j+1 < min) {
							min = j+1;
						}

					}
				}
			}
			System.out.println(max-min);
		}

	}

}
