package STUDY;

public class CaesarChipher {

	public static void main(String[] args) {
		String s = "a B z";
		String answer ="";
		int n = 4;
		char[] charArray = s.toCharArray();
		
		for(char spell: charArray) {
			if((int)spell == 32) {
				answer+=spell;
				continue;
			}
			int value = (int)spell + n;
			
			//대문자 
			if(Character.isUpperCase(spell) && 90 < value) {
				value -= 26;
			}else if(Character.isLowerCase(spell) && 122 < value) {//소문자
				value -= 26;
			}
			
			answer+= (char)value;
		}
		System.out.print(answer);
	}

}
