import java.util.Scanner;

public class inclass_practice{
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int n = input.nextInt(), s = 0, t =0;
		for (int i = 0; i <= n; ++i) {
			char line[] = input.nextLine().toLowerCase().toCharArray();
			for (char x :line) {
				if (x == 's') {
					s++;
				}else if (x == 't') {
					t++;
				}
			}
		}
		if (s>t) {
			System.out.println("French");
		}
		else if (s < t) {
			System.out.println("English");
		}else {
			System.out.println("French");
		}
	}
}
