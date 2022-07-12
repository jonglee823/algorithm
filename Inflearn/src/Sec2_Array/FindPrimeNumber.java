package Sec2_Array;

import java.util.Arrays;
import java.util.Scanner;

public class FindPrimeNumber {
	
	public int solution(int n) {
		int answer = 0;
		boolean[] primeArray = new boolean[n+1];
		Arrays.fill(primeArray, true);
		
		primeArray[0] = false;
		primeArray[1] = false;
		
		if (n <= 1) return 0;
		
		for(int i=2; (i*i)<=n; i++) {
			if(primeArray[i])
				for(int j=i*i; j<=n; j+=i) {
					primeArray[j] = false;
				}
		}
		
		for(boolean yn : primeArray) {
			if(yn) answer++;
		}
		
		return answer;
	}

	public static void main(String[] args) {
		FindPrimeNumber T = new FindPrimeNumber();
		Scanner kb = new Scanner(System.in);
		int n = kb.nextInt();
		
		System.out.println(T.solution(n));
		
	}
}