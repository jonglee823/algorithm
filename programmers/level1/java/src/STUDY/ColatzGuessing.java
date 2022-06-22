package STUDY;

public class ColatzGuessing {

	//프로그래머스 콜라츠 추측 LEVEL 1
	public static void main(String[] args) {
		long num = 626331;
		int answer = 0;
		  
		while(answer < 500) {
			if( num == 1) {
				break;
			}
			answer++;
			if( num % 2 ==0) {
				num /= 2;
			}else {
				num = (num * 3) +1;
			}	
		}
		
		if(num != 1) {
			answer = -1;
		}
	}	
}