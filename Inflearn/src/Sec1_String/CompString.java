package Sec1_String;

import java.util.Scanner;

/*
 * Inflearn java 알고리즘 
 * 2022년 07월 10일(sun)
 * 문자열 압축 하기 
 */
public class CompString {
	
	public String solution(String str) {
		String answer = null;
		StringBuffer sb = new StringBuffer();
		str = str +" ";
		
		int index = 1;	
		for(int i=0; i<str.length()-1; i++) {					
			if(str.charAt(i) == str.charAt(i+1)) index++;
			else {
				sb.append(str.charAt(i));
				if(index > 1) sb.append(index);
				index = 1;
			}
		}

		return sb.toString();
	}

	public static void main(String[] args) {
		CompString T = new CompString();
		Scanner kb = new Scanner(System.in);
		
		String str = kb.next();
		
		System.out.println(T.solution(str));
	}
}