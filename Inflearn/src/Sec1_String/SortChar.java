package Sec1_String;

import java.util.Arrays;
import java.util.Scanner;

public class SortChar {
	
	public int[] solution(String str, char t) {
		int answer = 0;
		int[] answerArray = new int[str.length()];
		
		//내가 짠 코드 start
		int charIndex = str.indexOf(t);
		int lt = charIndex;
		
		Arrays.fill(answerArray, 0);
		
		for(int i=0; i<str.length(); i++) {
			if(str.charAt(i) == t) {
				charIndex = i;
				
				int z=1;
				while(z < charIndex - lt) {
					answerArray[charIndex-z] = Math.min(answerArray[charIndex-z], z);
					z++;
				}
			}else {
				answerArray[i] = Math.abs(i - charIndex);
			}
		}
		//내가 짠 코드 end	
		
//		int p = 1000;
//		for(int i=0; i<str.length(); i++) {
//			if(str.charAt(i) == t) {
//				p = 0;
//				answerArray[i] = 0;
//			}else {
//				answerArray[i] = ++p;
//			}
//		}
//		p = 1000;
//		for(int i= str.length() -1; i>=0; i--) {
//			if(str.charAt(i) == t) p = 0;
//			else {
//				answerArray[i] = Math.min(answerArray[i], ++p);
//			}
//		}
		
		
		return answerArray;
	}
	

	public static void main(String[] args) {
		SortChar T = new SortChar();
		
		Scanner kb = new Scanner(System.in);
		
		String str = kb.next();
		char t = kb.next().charAt(0);
		
		long beforeTime = System.currentTimeMillis(); //코드 실행 전에 시간 받아오기
		System.out.println("beforeTime : " + beforeTime);
		for(int s : T.solution(str, t)) {
			System.out.print(s + " ");
		}
		
		long afterTime = System.currentTimeMillis();
		System.out.println("afterTime : " + afterTime);
		System.out.println("시간차이(m) : "+ (afterTime - beforeTime));
	}
}