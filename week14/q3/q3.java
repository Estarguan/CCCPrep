import java.util.*;

public class q3{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        Integer nums[] = new Integer[n];
        for (int i = 0; i < n; ++i){
            nums[i] = s.nextInt();
        }
        Arrays.sort(nums,(b,c) -> {
            return -Integer.compare(b,c);
        });
        Arrays.sort(nums,(b,c) -> {
            return Integer.compare(b%10,c%10);
        });
        for (int i : nums){
            System.out.print(i + " ");
        }
    }
}