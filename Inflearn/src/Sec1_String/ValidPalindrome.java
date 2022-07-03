package Sec1_String;

import java.util.Scanner;

public class ValidPalindrome {
	
	public String solution(String str) {
		String answer = "YES";
		str = str.toUpperCase().replaceAll("[^A-Z]", "");
		String temp = new StringBuilder(str).reverse().toString();
		
		if(!str.equals(temp)) return "NO";
		
		return answer;
	}

	public static void main(String[] args) {
		ValidPalindrome T = new ValidPalindrome();
		Scanner kb = new Scanner(System.in);
		String str = kb.nextLine();
		
		System.out.println(T.solution(str));
	}
}