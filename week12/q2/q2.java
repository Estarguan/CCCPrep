import java.util.Scanner;
public class q2{
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int h = input.nextInt(), m = input.nextInt();
		boolean ans = false;
		for (int t=1; t<=m;++t) {
			if (-6*Math.pow(t,4) + h * Math.pow(t,3)+2*Math.pow(t,2)+t <= 0) {
				System.out.println("The balloon first touches ground at hour:\n"+t);
				ans = true;
				break;
			}
		}
		if(!ans) {
			System.out.println("The balloon does not touch ground in the given time.");
		}
		input.close();
	}
}
