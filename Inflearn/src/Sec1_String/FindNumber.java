package Sec1_String;

import java.util.Scanner;

public class FindNumber {

	public int solution(String str) {
		int answer = 0;
		str = str.replaceAll("[^0-9]", "");
		answer = Integer.parseInt(str);
		
		return answer;
	}
	
	public static void main(String[] args) {
		FindNumber T = new FindNumber();
		Scanner kb = new Scanner(System.in);
		String str = kb.next();
		
		System.out.println(T.solution(str));
		

	}

}
