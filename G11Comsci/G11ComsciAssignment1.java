import java.util.Scanner;

public class G11ComsciAssignment1 {

	public static void main(String[] args) {
		// Estar Guan Mon Sep 11, 2023
		//This is my code for running my desert store
		Scanner scan = new Scanner(System.in);
		System.out.println("WELCOME TO MY YUMMY-IN-THE-TUMMY DESSERT PLACE");
		int bobas = 0 , icecreams= 0, cookies=0, cupcake=0, macaroons=0;
		
		boolean inputting = true;
		while (inputting) {
			try {
				//inputs
				System.out.print("How many bobas would you like?  ");
				bobas = Integer.parseInt(scan.nextLine ());
				System.out.print("How many icecreams would you like?  ");
				icecreams = Integer.parseInt(scan.nextLine ());
				System.out.print("How many cookies would you like?  ");
				cookies = Integer.parseInt(scan.nextLine ());
				System.out.print("How many cupcakes would you like?  ");
				cupcake = Integer.parseInt(scan.nextLine ());
				System.out.print("How many macaroons would you like?  ");
				macaroons = Integer.parseInt(scan.nextLine ());
				inputting = false;
			} catch (Exception e) {
				System.out.println("Please input a valid amount");
				
			}
		}
		
		//calculations
		double bobaCost = Math.round(4.67*bobas*100)/100.0;
		double icecreamCost = Math.round(6.81*icecreams*100)/100.0;
		double cookieCost = Math.round(5.29*cookies*100)/100.0;
		double cupcakeCost = Math.round(4.42*cupcake*100)/100.0;
		double macaroonCost = Math.round(5.15*macaroons*100)/100.0;
		
		
		
		
		//Cost
		System.out.printf(bobas + " bobas @ $4.67 each = $%.2f%n",bobaCost);
		System.out.printf(icecreams + " icecreams @ $6.81 each = $%.2f%n",icecreamCost);
		System.out.printf(cookies + " cookies @ $5.29 each = $%.2f%n",cookieCost);
		System.out.printf(cupcake + " cupcakes @ 4.42 each = $%.2f%n",cupcakeCost);
		System.out.printf(macaroons + " macaroons @ 5.15 each = $%.2f%n%n",macaroonCost);
		
		//Final Costs
		System.out.println("Total = $" + Math.round((bobaCost+icecreamCost+cookieCost+macaroonCost+cupcakeCost)*100)/100.0);
		double discountTotal = Math.round((3.405*icecreams+ 3.736*bobas + 4.232*cookies + 3.536*cupcake + 4.12*macaroons)*100)/100.0;
		System.out.println("Total with discount $" + discountTotal);
		double finalTotal = Math.round(discountTotal*1.13*100)/100.0;
		System.out.println("Total with tax $" + finalTotal);
		
		
		//payment
		System.out.print("\nPlease enter the amount to be paid:  $");
		double payment = scan.nextDouble();
		while (payment < finalTotal) {
			System.out.print("You need to pay at least $" + finalTotal + "  $");
			payment = scan.nextDouble();
		}
		double change = Math.round((payment-finalTotal)*100)/100.0;
		System.out.println("The change will be:\t$" + change);
		
		//change calculations 
		//fifties and twenties
		System.out.println("\nTo make up this amount, you will need:");
		int fifties = (int)(change/50);
		change -= 50*fifties;
		change= Math.round(change*100)/100.0;
		int twenties = (int)(change/20);
		change -= twenties * 20;
		change= Math.round(change*100)/100.0;		
		System.out.printf("%4d  %-18s%4d  %s%n",fifties,"fifty-dollar bills",twenties,"twenty-dollar bills");
		
		//tens and fives
		int tens = (int)(change/10);
		change -= 10*tens;
		change= Math.round(change*100)/100.0;
		int fives = (int)(change/5);
		change -= 5*fives;
		change= Math.round(change*100)/100.0;
		System.out.printf("%4d  %-18s%4d  %s%n",tens,"ten-dollar bills",fives,"five-dollar bills");
		
		//toonies and loonies
		int toonies = (int)(change/2);
		change -= 2*toonies;
		change= Math.round(change*100)/100.0;
		int loonies = (int)(change/1);
		change -= loonies;
		change= Math.round(change*100)/100.0;
		
		System.out.printf("%4d  %-18s%4d  %s%n",toonies,"toonies",loonies,"loonies");
		
		//quarters and dimes
		int quarters = (int)(change/0.25);
		change -= 0.25*quarters;
		change= Math.round(change*100)/100.0;
		int dimes = (int)(change/0.1);
		change -= 0.1*dimes;
		System.out.printf("%4d  %-18s%4d  %s%n",quarters,"quarters",dimes,"dimes");
		
		//nickels and pennies
		int nickels = (int)(change/0.05);
		change -= 0.05*nickels;
		change= Math.round(change*100)/100.0;
		int pennies = (int)(change/0.01);
		change -= 0.01*pennies;
		change= Math.round(change*100)/100.0;
		System.out.printf("%4d  %-18s%4d  %s%n",nickels,"nickels",pennies,"pennies");
		
		
		scan.close();
	}
	
}
