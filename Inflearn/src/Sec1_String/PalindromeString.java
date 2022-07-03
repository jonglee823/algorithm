package Sec1_String;

import java.util.Scanner;

public class PalindromeString {
	
	public String solution(String str) {
		String answer = "YES";
		
		int lt=0;
		int rt=str.length()-1;
		
		
		
		String temp = new StringBuilder(str).reverse().toString();
		if(!temp.equalsIgnoreCase(str)) return "NO";
		
		//내가 푼거 start
		//str = str.toLowerCase();
//		while(lt<rt) {
//			if(str.charAt(lt) != str.charAt(rt)) {
//				answer = "NO";
//				break;
//			}else {
//				lt++;
//				rt--;
//			}
//		}
		//내가 푼거 End
		
		
		return answer;
	}

	public static void main(String[] args) {
		PalindromeString T = new PalindromeString();
		Scanner kb = new Scanner(System.in);
		
		String str = kb.next();
		
		System.out.println(T.solution(str));

	}
}