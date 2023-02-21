import java.util.Scanner;

public class q4{
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int k;
		k = input.nextInt();
		char[] str = input.next().toCharArray();
		for (int i = 0; i < str.length; ++i) {
			int x = (int)str[i] - (3*(i+1)+k);
			if (x < 65) {
				x = 90-(65-(x+1));
				System.out.print((char)x);
			}else {
				System.out.print((char)x);
			}
			input.close();
		}
	}
}
