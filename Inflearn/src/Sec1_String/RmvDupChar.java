package Sec1_String;

import java.util.Iterator;
import java.util.LinkedHashSet;
import java.util.Scanner;

public class RmvDupChar {
	
	public String solution(String str) {
		
		StringBuilder answer = new StringBuilder(str.length());
		
		
		LinkedHashSet hashSet = new LinkedHashSet();
		
		for(char a : str.toCharArray()) {
			hashSet.add(a);
		}
	
		Iterator it = hashSet.iterator();
		while(it.hasNext()) {
			answer.append(it.next());
		}
		
		return answer.toString();
		
	}

	public static void main(String[] args) {
		RmvDupChar T = new RmvDupChar();
		Scanner kb = new Scanner(System.in);
		
		String str = kb.next();
		
		System.out.println(T.solution(str));
		

	}

}
