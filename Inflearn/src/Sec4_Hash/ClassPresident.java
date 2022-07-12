package Sec4_Hash;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class ClassPresident {

	public char solution(String str) {
		Map<Character, Integer> map = new HashMap<>();
		char answer = ' ';
		
		for(char a : str.toCharArray()) {
			map.put(a, map.getOrDefault(a, 0) +1);
		}
				
//		Comparator<Entry<Character, Integer>> comparator = new Comparator<Entry<Character, Integer>>(){
//			@Override
//			public int compare(Entry<Character, Integer> e1, Entry<Character, Integer>e2) {
//				return e1.getValue().compareTo(e2.getValue());
//			}
//		};
//		
//		Entry<Character, Integer> maxEntry = Collections.max(map.entrySet(), comparator);
//		String answer = maxEntry.getKey().toString();
		
		int max = Integer.MIN_VALUE;
		for(char key : map.keySet()) {
			if(map.get(key) > max) {
				max = map.get(key);
				answer = key;
			}
		}
		
		return answer;
	}
	
	public static void main(String args[]) {
		ClassPresident T = new ClassPresident();
		
		Scanner kb = new Scanner(System.in);
		int n = kb.nextInt();
		String str = kb.next();
		System.out.println(T.solution(str));
	}
}