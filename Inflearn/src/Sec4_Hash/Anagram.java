package Sec4_Hash;

import java.util.HashMap;
import java.util.Scanner;

public class Anagram {
	
	public String solution(String str1, String str2) {
		
		HashMap<Character, Integer>map1 = new HashMap<>();
		HashMap<Character, Integer>map2 = new HashMap<>();
		
		for(char a: str1.toCharArray()) {
			map1.put(a, map1.getOrDefault(a, 0) +1);
		}
		
		for(char a: str2.toCharArray()) {
			map2.put(a, map2.getOrDefault(a, 0) +1);
		}
		
		if(map1.equals(map2)) {
			return "YES";
		}else {
			return "NO";
		}
	}

	public static void main(String[] args) {
		Anagram T = new Anagram();
		Scanner kb = new Scanner(System.in);
		
		String str1 = kb.next();
		String str2 = kb.next();
		
		System.out.println(T.solution(str1, str2));
	}

}
