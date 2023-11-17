package Sec2_Array;

import java.util.Scanner;

public class Fibonacci {

	public void solution(int num) {
		String answer ="";
		int[] numArray = new int[num + 1];
		
		numArray[1] = 1;
		numArray[2] = 1;
		numArray[3] = 2;
		
		if(num > 3) {
			for(int i=3; i<=num; i++) {
				numArray[i] = numArray[i-2] + numArray[i-1];
			}
		}
		
		for(int i=1; i<numArray.length; i++) {
			System.out.print(numArray[i] + " ");
		}		
	}
	
	
	public static void main(String[] args) {
		Fibonacci T = new Fibonacci();
		
		Scanner kb = new Scanner(System.in);
		
		int num = kb.nextInt();
		
		T.solution(num);

	}
}