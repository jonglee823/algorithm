package Sec2_Array;

import java.util.Scanner;

//2022.08.02 가위바위 보 게임 결과 출력하기
//1 가위
//2 바위
//3 보 
//1 2 B
//1 3 A
//2 1 A
//2 3 B
//3 1 B
//3 2 B
public class GameResult {
	
	public void solution(int n, int[] aArray, int[] bArray) {
		
		for(int i=0; i<n; i++) {
			if(aArray[i] == bArray[i]) {
				System.out.println("D");
			}else if(aArray[i] == 1 && bArray[i] == 3) {
				System.out.println("A");
			}else if(aArray[i] == 2 && bArray[i] == 1) {
				System.out.println("A");
			}else if(aArray[i] == 3 && bArray[i] == 2) { //aArray[i] == 3
				System.out.println("A");
			}else {
				System.out.println("B");
			}
		}
	}

	public static void main(String[] args) {
		GameResult T = new GameResult();
		Scanner kb = new Scanner(System.in);
		
		int n = kb.nextInt();
		int[] bArray = new int[n];
		int[] aArray = new int[n];
		
		for(int i=0; i<n; i++) {
			aArray[i] = kb.nextInt();
		}
		
		for(int i=0; i<n; i++) {
			bArray[i] = kb.nextInt();
		}
		
		T.solution(n, aArray, bArray);

	}
}