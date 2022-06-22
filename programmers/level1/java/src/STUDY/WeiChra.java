package STUDY;

public class WeiChra {
	//프로그래머스 1단계 이상한 문자 만들기
	
	public static void main(String[] args) {
		String s = "try hello  world";
		char[] charArray = s.toCharArray();
		String answer ="";
		
		StringBuilder strBuilder = new StringBuilder(s.length());
		
		int index = 0;
		for(char spell: charArray) {
			if((int) spell == 32) {
				strBuilder.append(" ");
				index = 0;
			}else {
				if(index % 2 == 0) {
					spell = Character.toUpperCase(spell);
				}else {
					spell = Character.toLowerCase(spell);
				}
				strBuilder.append(spell);
				++index;
			}
		}
		answer=strBuilder.toString();
	}
}
