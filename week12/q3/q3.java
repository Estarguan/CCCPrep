import java.util.Scanner;

public class HelloWorld{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int t1 = input.nextInt(), t2 = input.nextInt();
        int diff = t1-t2, num = 2;
        while (diff >= 0){
            int temp = diff;
            diff = t2 - diff;
            t2 = temp;
            num++;
        }
        System.out.println(num);

    }
}
