package Sec1_String;

import java.util.Scanner;

public class ReverseWord {
	
	
	public void solution(String[] strArray) {
		
		for(String str : strArray) {
			StringBuilder sb = new StringBuilder(str);
			System.out.println(sb.reverse());
		}
	}

	public static void main(String[] args) {
		ReverseWord T = new ReverseWord();
		Scanner kb = new Scanner(System.in);
		
		int n = kb.nextInt();
		String[] strArray = new String[n];
		
		for(int i=0; i<n; i++) {
			strArray[i] = kb.next();
		}
		
		
		
		T.solution(strArray);

	}

}
