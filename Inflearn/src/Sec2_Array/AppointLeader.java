package Sec2_Array;

import java.util.Scanner;

public class AppointLeader {
	
	public int solution(int[][] intArray, int count) {

		int answer=0, max = Integer.MIN_VALUE;
				
		//i man
		for(int i=0; i<count; i++) {
			int cnt=0;
			for(int j=i; j<count; j++) {
				for(int k=0; k<5; k++) {
					if(intArray[i][k] == intArray[j][k]) {
						cnt++;
						break;
					}
				}
			}			
			if(cnt > max) {
				max = cnt;
				answer =i;
			}
		}

		return (answer+1);
		
	}

	public static void main(String[] args) {
		AppointLeader T = new AppointLeader();
		Scanner kb = new Scanner(System.in);
		int count = kb.nextInt();
		int[][] intArray = new int[count][5];
		
		for(int i=0; i<count; i++) {
			for(int j=0; j<5; j++) {
				intArray[i][j] = kb.nextInt();
			}
		}
		
		System.out.println(T.solution(intArray, count));

	}
}