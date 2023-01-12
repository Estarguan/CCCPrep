import java.util.Scanner;
public class q3 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int k = input.nextInt();
		String ans1 = "", ans2 = "", ans3 ="";
		String[][] icon = {
    			{
    				"*", "x", "*"
    			},
    			{
    				" ", "x", "x"
    			},
    			{
    				"*", " ", "*"
    			}
    	};
		for (int x = 0; x < 3; ++x) {
			for (int y = 0; y < 3; ++y) {
				if (x == 0) {
					ans1 += icon[x][y].repeat(k);
				}else if (x==1) {
					ans2 += icon[x][y].repeat(k);
				}else {
					ans3 += icon[x][y].repeat(k);
				}
			}
		}
		for (int i = 0; i < k; ++i) {
			System.out.println(ans1);
		}
		for (int i = 0; i < k; ++i) {
			System.out.println(ans2);
		}
		for (int i = 0; i < k; ++i) {
			System.out.println(ans3);
		}
		input.close();
	}

}
