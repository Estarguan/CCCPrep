import java.util.Scanner;
public class randomTesting {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner input = new Scanner(System.in);
		int f1, f2, f3, f4;
		f1 = input.nextInt();
		f2 = input.nextInt();
		f3 = input.nextInt();
		f4 = input.nextInt();
		if (f1==f2  && f2== f3 && f3==f4) {
			System.out.println("Fish At Constant Depth");
		}else if ( f1<f2 && f2<f3 && f3<f4) {
			System.out.println("Fish Rising");
		}else if (f1 > f2 && f2 > f3 && f3 > f4) {
			System.out.println("Fish Diving");
		}else {
			System.out.println("No Fish");
		}
	}

}
