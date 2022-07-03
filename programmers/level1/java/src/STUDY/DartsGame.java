package STUDY;

/*
 * 프로그래머스 LEVEL1 다트 게임 
 * 2022.07.01
 */
public class DartsGame {

	public static void main(String[] args) {
		
		//입력값 start
		/* SCORE|BONUS|OPTIONS
		 * SCORE 0~10
		 * BONUS * S 1제곱, * D 2제곱 ,T 3제곱
		 * OPTIONS *: 해당점수, 그전점수 2 ,# : 해당 점수 - 
		 */
		String dartResult = "1D2S#10S";
		//입력값 end
		
		int answer = 0;
		
		String[] strCore = dartResult.split("[+0-9]");
		String[] numCore = dartResult.replaceAll("[^0-9]", "").split("");
		Integer[] tempCore = new Integer[numCore.length];
		
		for(int i=0; i<strCore.length; i++) {
			System.out.println("strCore : " + strCore[i]);
		}
		
		for(int i=0; i<numCore.length; i++) {
			System.out.println("numCore : " + numCore[i]);
		}
		
		
		for(int i=0; i<numCore.length; i++) {
			Integer tempScore = Integer.parseInt(numCore[i]);
			String str = strCore[i+1];
			if(str.contains("D")) tempScore = (int) Math.pow(tempScore, 2);
			else if(str.contains("T")) tempScore = (int) Math.pow(tempScore, 3);
			
			if(str.contains("#")) tempScore *= -1;
			else if(str.contains("*")) {
				tempScore *= 2;
				if(i > 0) {
					tempCore[i-1] = tempCore[i-1] * 2;
				}
			}
			tempCore[i] = tempScore;
		}
		for(Integer score : tempCore) {
			answer += score;
			System.out.println("score : " + score);
		}
		System.out.println(answer);
	}

}
