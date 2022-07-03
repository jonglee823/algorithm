package Sec3_TwoPointer;

import java.util.Scanner;

public class CotinuSubSequence {
	
	public int solution(int n, int m, int[] num1) {
		int answer =0;
		int sum = 0;
		
		int lt=0;
		
		int p1=0, p2=0;
	
		for(int rt=0; rt<n; rt++) {
			sum += num1[rt];
			if(sum==m) {
				answer++;
				System.out.println("lt : " + lt + " rt : " + rt);
			}
			while(sum >=m) {
				sum -=num1[lt++];
				if(sum == m) {
					answer++;
					System.out.println("lt : " + lt + " rt : " + rt);
				}
			}
			
		}
		
		return answer;
	}

	public static void main(String[] args) {
		CotinuSubSequence T = new CotinuSubSequence();
		
		Scanner kb = new Scanner(System.in);
		
		int n = kb.nextInt();
		
		int m = kb.nextInt();
		
		int[] num = new int[n];
		for(int i=0; i<n; i++) {
			num[i] = kb.nextInt();
		}
		
		System.out.println(T.solution(n, m, num));

	}

}
