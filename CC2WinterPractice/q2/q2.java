import java.util.Scanner;
public class q2{
    public static void main(String[] args){
    	Scanner s = new Scanner(System.in);
    	int n = s.nextInt();
    	String cows;
    	if (n >= 1000) {
    		cows = "moo".repeat(1000);
    	}else {
    		cows = "moo".repeat(n);
    	}
    	String sub = s.next();
    	if (cows.contains(sub)) {
    		System.out.println("yes");
    	}else {
    		System.out.println("no");
    	}
    }
}