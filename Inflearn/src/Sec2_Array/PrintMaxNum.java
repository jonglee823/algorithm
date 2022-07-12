package Sec2_Array;

import java.util.Scanner;

public class PrintMaxNum {
	
	public void solution(int[] array) {
		
		int lt=0;
		System.out.print(array[lt]);
		for(int i=1; i<array.length; i++) {
			if(array[lt++] < array[i]) {
				System.out.print(" " + array[i]);
			}
		}
	}

	public static void main(String[] args) {
		PrintMaxNum T = new PrintMaxNum();
		Scanner kb = new Scanner(System.in);
		
		int n = kb.nextInt();
		int[] array = new int[n];
		for(int i=0; i<n; i++) {
			array[i] = kb.nextInt();
		}
		
		T.solution(array);

	}

}
