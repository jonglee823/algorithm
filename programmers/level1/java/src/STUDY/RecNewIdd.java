package STUDY;

import java.util.regex.Matcher;
import java.util.regex.Pattern;
 
/* 프로그래머스 LEVEL1 신규 아이디 추천
 * 2022.06.27
 * 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
 * 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
 * 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
 * 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
 * 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
 * 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
 * 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
 * 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
 */
public class RecNewIdd {

	public static void main(String[] args) {
		String new_id = "abcdefghijklmn.p";
		String answer = "";
		
		StringBuilder sb = new StringBuilder(new_id.length());
				
		sb.append(new_id);
				
		//1st
		for(int i =0; i<sb.length(); i++) {
			sb.setCharAt(i, Character.toLowerCase(sb.charAt(i)));
		}
		
		//2st
		sb = replaceAll(sb, "[^a-z0-9-_.]", "");
		
		//3st
		sb = replaceAll(sb, "[.]{2,}", ".");
		
		//4st
		sb = replaceAll(sb, "^[.]|[.]$", "");
		System.out.println("4st : " + sb);
		
		//5st
		if(sb.length() == 0) {
			sb.append("a");
		}		
		
		//6st
		if(sb.length() >= 16) {
			sb.replace(15, sb.length(), "");
			sb = replaceAll(sb, "[.]$", "");
		}
		
		//7st
		while(sb.length() <= 2) {
			sb.append(sb.charAt(sb.length()-1));
		}
		answer = sb.toString();
	}
	
	public static StringBuilder replaceAll(StringBuilder sb, String regex, String replacement) {
		Pattern pattern = Pattern.compile(regex);
		Matcher m = pattern.matcher(sb);
		int start = 0;
		while(m.find(start)) {
			sb.replace(m.start(), m.end(), replacement);
			start = m.start() + replacement.length();
		}
		return sb;
	}
}
