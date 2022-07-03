package Sec1_String;

import java.util.Scanner;

public class RvsOnlyAlpha {

	public String solution(String str) {
		String answer = null;
		
		int lt =0;
		int rt = str.length()-1;
		char[] charArray = str.toCharArray();
		
		while(lt < rt) {
			
			if(!Character.isAlphabetic(str.charAt(rt))) {
				rt--;
			}
			
			if(!Character.isAlphabetic(str.charAt(lt))) {
				lt++;
			}
			
			if(Character.isAlphabetic(str.charAt(lt)) && Character.isAlphabetic(str.charAt(rt))) {
				char temp = str.charAt(lt);
				charArray[lt++] = charArray[rt];
				charArray[rt--] = temp;
			}
		}
		return new String(charArray);
	}
	
	public static void main(String args[]) {
		RvsOnlyAlpha T = new RvsOnlyAlpha();
		
		Scanner kb = new Scanner(System.in);
		
		String str = kb.next();
		
		System.out.println(T.solution(str));
	}
}
