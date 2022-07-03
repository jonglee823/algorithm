package Sec1_String;

import java.util.Scanner;

public class ChgStrCase {
	
	public String solution(String str) {
		StringBuilder sb = new StringBuilder(str.length());
		
		for(char a : str.toCharArray()) {
			
			if(64 < a && a < 97) {
				a += 32;
			}else if(96 < a && a < 121){
				a -= 32;
			}
			sb.append(a);
		}
		return sb.toString();
	}
	
	

	public static void main(String[] args) {
		ChgStrCase T = new ChgStrCase();
		Scanner kb = new Scanner(System.in);
		String str = kb.nextLine();
		System.out.println(T.solution(str));
	}

}
