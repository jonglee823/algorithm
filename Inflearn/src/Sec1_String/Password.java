package Sec1_String;

import java.util.Scanner;

/*
 * Inflearn java 알고리즘 
 * 문자열 *, #을 0,1으로 바꾼뒤 ASCII로 변환
 * 2022.07.10(SUN)
 */
public class Password {
	
	public String solution(int count, String str) {
		StringBuffer sb = new StringBuffer();
		
		str = str.replaceAll("#", "1").replaceAll("\\*", "0");

		int index =0;
		while(index < count) {
			sb.append((char)(Integer.parseInt(str.substring(index*7, (index+1)*7), 2)));
			index++;
		}
		
		return sb.toString();
	}

	public static void main(String[] args) {
		Password T = new Password();
		Scanner kb = new Scanner(System.in);
		
		int count = kb.nextInt();
		String str = kb.next();
		System.out.println(T.solution(count, str));
	
	}
}