package Sec2_Array;

import java.util.Scanner;

public class ReversePrime {
	
	public void solution(int n, int[] intArray) {
		
		for(int i=0; i<n; i++) {
			for(;;) {
				if(intArray[i]%10 == 0) {
					intArray[i] = intArray[i]%10;
				}else {
					System.out.println(intArray[i]);
					continue;
				}
			}
			
			
		}
	}
	
	public static void main(String[] args) {
		ReversePrime T = new ReversePrime();
		Scanner kb = new Scanner(System.in);
		
		int n = kb.nextInt();
		int[] intArray = new int[n+1];
		
		for(int i=0; i<n; i++) {
			intArray[i] = kb.nextInt();
		}
		
		T.solution(n, intArray);
	}

}
