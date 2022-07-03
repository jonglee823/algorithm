package Sec1_String;


import java.util.Scanner;

public class FindString {
	public int solution(String str, char t) {
		int answer =0;
		str = str.toLowerCase();
		t = Character.toLowerCase(t);
		
		for(char a : str.toCharArray()) {
			if(a == t) {
				answer +=1;
			}
		}
		
		return answer;
	}
	

	public static void main(String[] args) {
		FindString findString = new FindString();
		Scanner kb = new Scanner(System.in);
		String str = kb.nextLine();
		char find_str = kb.nextLine().charAt(0);

		
		System.out.println(findString.solution(str, find_str) + "");
	}

}
