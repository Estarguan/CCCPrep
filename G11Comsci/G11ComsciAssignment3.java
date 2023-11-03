
import java.util.*;
import java.io.*;

public class G11ComsciAssignment {

	public static void main(String[] args) throws IOException,FileNotFoundException{
		//Estar Guan Period 2 Assignment 3 Monday October 30 2023
		//to do fix step 5 odd letters
		
		String 	 runAgain = "Y";
		String originals = "BFASTUWDMOE ";
		String substitutes = "!@#$%^&*()=?";
		Scanner scan = new Scanner(System.in);
		
		do {
			

			String choice;
			do {
				System.out.println("Do you want to Encrypt or Decrypt");
				choice = scan.nextLine();
			}while(!choice.equalsIgnoreCase("Encrypt") && !choice.equalsIgnoreCase("Decrypt"));
			
			System.out.println("What is the name of your input file?");
			String inputFile = scan.nextLine();
			
			System.out.println("What is the name of your output file?");
			String outputFile = scan.nextLine();
			
			System.out.println("What is the key?");
			int key = Integer.parseInt(scan.nextLine());
			
			Scanner inFile = new Scanner (new FileReader(inputFile));
			PrintWriter outFile = new PrintWriter(new FileWriter (outputFile));
			if (choice.equalsIgnoreCase("encrypt")) {
				while (inFile.hasNextLine()) {
					String line = inFile.nextLine();
					
					//step 1
					int leadingSpaces = 0, trailingSpaces = 0;
					if (line.charAt(0) == ' ') {
						int i = 0;
						while (line.charAt(i) == ' ') {
							leadingSpaces++;
							i++;
						}
						
					}if (line.charAt(line.length()-1) == ' ') {
						int i = line.length()-1;
						while (line.charAt(i) == ' ') {
							trailingSpaces++;
							i--;
						}
					}
					
					//step 2
					line = line.substring(leadingSpaces,line.length()-trailingSpaces).toUpperCase();
					
//					//step 3
//					
					for (int i = 0; i < line.length(); i++) {
						if (key > 0) {
							key %= 12;
							if (originals.indexOf(line.charAt(i))!= -1) {
								if (originals.indexOf(line.charAt(i))+ key > 11) {
									line = line.substring(0,i) + substitutes.charAt(originals.indexOf(line.charAt(i))+ key-12) + line.substring(i+1);
								}else {
									line = line.substring(0,i) + substitutes.charAt(originals.indexOf(line.charAt(i))+ key) + line.substring(i+1);							

								}
							}
						}else {
							key %= 12;
							if (originals.indexOf(line.charAt(i))!= -1) {
								if (originals.indexOf(line.charAt(i)) + key < 0) {
									line = line.substring(0,i) + substitutes.charAt(originals.indexOf(line.charAt(i))+ key+12) + line.substring(i+1);
								}else {
									line = line.substring(0,i) + substitutes.charAt(originals.indexOf(line.charAt(i)) + key) + line.substring(i+1);							

								}
							}
						}
					}
					
					//step 4
					String firstTwo = line.substring(0,2);
					String lastTwo = line.substring(line.length()-2);
					line = lastTwo + line.substring(2,line.length()-2) + firstTwo;
					
					//step 5
					if (line.length()%2 == 0) {
						line = line.substring(line.length()/2) + line.substring(0,line.length()/2);
					}else {
						line = line.substring(line.length()/2+1) + line.substring(0,line.length()/2+1);
					}
					
					//step 6
					if (line.length()%2 == 0) {
						line = line.substring(0,line.length()/2-3) + line.substring(line.length()/2-1, line.length()/2+1) + line.substring(line.length()/2-3,line.length()/2-1) + line.substring(line.length()/2+1);
					}else {
						line = line.substring(0,line.length()/2-2) + line.substring(line.length()/2, line.length()/2+2) + line.substring(line.length()/2-2,line.length()/2) + line.substring(line.length()/2+2);
					}
					
					//step 7
					int i = 0;
					if (line.length() %2 == 0) {
						while (i < line.length()) {
							line = line.substring(0,i) + line.charAt(i+1) + line.charAt(i)+ line.substring(i+2);
							i += 2;
						}
					}else {
						while (i < line.length()-1) {
							line = line.substring(0,i) + line.charAt(i+1) + line.charAt(i)+ line.substring(i+2);
							i += 2;
						}
					}
					outFile.println(line);
					outFile.println(leadingSpaces);
					outFile.println(trailingSpaces);
					
				
				}
				outFile.close();
				inFile.close();
			}else{
				key = -key;
				while (inFile.hasNextLine()) {
					String line = inFile.nextLine();
					//leading and trailing spaces
					int leadingSpaces = Integer.parseInt(inFile.nextLine());
					int trailingSpaces = Integer.parseInt(inFile.nextLine());
					
					for (int i = 0; i < leadingSpaces; i++) {
						outFile.print(' ');
					}
					
					
					//undo step 7
					
					int j = 0;
					if (line.length() %2 == 0) {
						while (j < line.length()) {
							line = line.substring(0,j) + line.charAt(j+1) + line.charAt(j)+ line.substring(j+2);
							j += 2;
						}
					}else {
						while (j < line.length()-1) {
							line = line.substring(0,j) + line.charAt(j+1) + line.charAt(j)+ line.substring(j+2);
							j += 2;
						}
					}
//					
					//undo step 6
					if (line.length()%2 == 0) {
						line = line.substring(0,line.length()/2-3) + line.substring(line.length()/2-1, line.length()/2+1) + line.substring(line.length()/2-3,line.length()/2-1) + line.substring(line.length()/2+1);
					}else {
						line = line.substring(0,line.length()/2-2) + line.substring(line.length()/2, line.length()/2+2) + line.substring(line.length()/2-2,line.length()/2) + line.substring(line.length()/2+2);
					}
//					
					//undo step 5
					if (line.length()%2 == 0) {
						line = line.substring(line.length()/2) + line.substring(0,line.length()/2);
					}else {
						line = line.substring(line.length()/2) + line.substring(0,line.length()/2);
					}
					
					//undo step 4
					String firstTwo = line.substring(0,2);
					String lastTwo = line.substring(line.length()-2);
					line = lastTwo + line.substring(2,line.length()-2) + firstTwo;
					
					
					
					//undo step 3
					for (int i = 0; i < line.length(); i++) {
						if (key > 0) {
							key %= 12;
							if (substitutes.indexOf(line.charAt(i))!= -1) {
								if (substitutes.indexOf(line.charAt(i))+ key > 11) {
									line = line.substring(0,i) + originals.charAt(substitutes.indexOf(line.charAt(i))+ key-12) + line.substring(i+1);
								}else {
									line = line.substring(0,i) + originals.charAt(substitutes.indexOf(line.charAt(i))+ key) + line.substring(i+1);							

								}
							}
						}else {
							key %= 12;
							if (substitutes.indexOf(line.charAt(i))!= -1) {
								if (substitutes.indexOf(line.charAt(i)) + key < 0) {
									line = line.substring(0,i) + originals.charAt(substitutes.indexOf(line.charAt(i))+ key+12) + line.substring(i+1);
								}else {
									line = line.substring(0,i) + originals.charAt(substitutes.indexOf(line.charAt(i)) + key) + line.substring(i+1);							

								}
							}
						}
					}
					
					//undo step 2
					line = line.toLowerCase();
					
					//output
					outFile.print(line);
					
					for (int i = 0; i < trailingSpaces; i++) {
						outFile.print(' ');
					}
					outFile.println(" ");
				}
				outFile.close();
				inFile.close();
			
			}
			//Check whether to run the code again
			
			do {
				System.out.println("Do you want to go again? Y/N");
				runAgain = scan.nextLine();
			}while (!runAgain.equalsIgnoreCase("Y") && !runAgain.equalsIgnoreCase("N"));
			
		}while(runAgain.equalsIgnoreCase("Y"));
	}

}
