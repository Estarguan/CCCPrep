import java.util.*;
public class q4 {
	public static void main(String[] args){
		Scanner s = new Scanner(System.in);
		int hunger = s.nextInt(), apples = s.nextInt(), wait = s.nextInt(), bar = 0;
		bar = (apples > hunger) ? hunger:apples;
		bar = (bar - wait < 0) ? 0 : bar-wait;
		System.out.println(bar);
		s.close();
	}
}
