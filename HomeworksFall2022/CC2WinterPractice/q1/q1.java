import java.util.Scanner;
public class randomStuff{
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		int n = s.nextInt();
		for (int i = 0; i < n; ++i) {
			String num = s.next();
			int sum = 0;
			for (Character j : num.toCharArray()) {
				sum += Integer.parseInt(j.toString());
			}
			if (sum % 3 == 0) {
				System.out.println("yes");
			}else {
				System.out.println("no");
			}
		}
	}
}