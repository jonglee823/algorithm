package Sec1_String;

import java.util.Scanner;
public class FindLongString {

	public String solution(String[] str) {
		String answer = null;
		int tempSize = str[0].length();
		int index = 0;
		
		for(int i=1; i<str.length; i++) {
			if(tempSize < str[i].length()) {
				tempSize = str[i].length();
				index = i;
			}
		}
		
		return str[index];
		
	}
	
	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		FindLongString T = new FindLongString();
		String[] str = kb.nextLine().split(" ");	
		
		System.out.print(T.solution(str));
	}
}
