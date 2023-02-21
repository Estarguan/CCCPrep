import java.util.Scanner;

public class q1{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int ant = input.nextInt(), eye = input.nextInt();
        if (ant >= 3 && eye <= 4){
            System.out.println("TroyMartian");
        }
        if (ant <= 6 && eye >= 2){
            System.out.println("VladSaturnian");
        }
        if (ant <= 2 && eye <= 4){
            System.out.println("GraemeMercurian");
        }
        input.close();
    }
}
