import java.util.*;

public class q2 {
  public static void main(String[] args){
    Scanner s = new Scanner(System.in);
    int n = s.nextInt();
    int[] trees = new int[n];
    for (int i = 0; i < n; ++i){
      trees[i] = s.nextInt();
    }
		int maxlen = 0, length = 1;
		for (int i = 0; i < n - 1; ++i){
			if (trees[i] < trees[i+1]){
				length++;
			}else{
				if (length > maxlen){
					maxlen = length;
				}
				length=1;
			}
		}
		if (length > maxlen)
		{maxlen = length;}
		System.out.println(maxlen);
		maxlen = 0; length = 1;
		for (int i = 0; i < n - 1; ++i){
			if (trees[i] > trees[i+1]){
				length++;
			}else{
				if (length > maxlen){
					maxlen = length;
				}
				length = 1;
			}
		}
		if (length > maxlen)
		{maxlen = length;}
		System.out.println(maxlen);
		s.close();
  }
}
