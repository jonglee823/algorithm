package Sec3_TwoPointer;


import java.util.Scanner;
public class MaxSales {
	
	public int solution(int[] sal, int k) {
		int answer=0, sum=0;
		for(int i=0; i<k; i++) {
			answer += sal[i];
		}
		
		sum = answer;
		for(int i=k; i<sal.length; i++) {
			sum += sal[i] - sal[i-k];
			answer = Math.max(answer, sum);		
		}
		return answer;
	}

	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		MaxSales T = new MaxSales();
		
		int n = kb.nextInt();
		int k = kb.nextInt();
		int[] sal = new int[n];
		for(int i=0; i<n; i++) {
			sal[i] = kb.nextInt();
		}
		
		System.out.println(T.solution(sal, k));
		
	}
}
