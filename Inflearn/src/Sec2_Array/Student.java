package Sec2_Array;

import java.util.Scanner;

public class Student {
	
	public int solution(int n, int[] array) {
		int answer = 1;
		int max = array[0];
		
		for(int i=1; i<n; i++) {
			if(array[i] > max) {
				answer++;
				max = array[i];
			}
		}
		
		return answer;
	}

	public static void main(String[] args) {
		Student T = new Student();
		Scanner kb = new Scanner(System.in);

		int n = kb.nextInt();
		int array[] = new int[n];
		
		
		for(int i=0; i<n; i++) {
			array[i] = kb.nextInt();
		}
		
		System.out.println(T.solution(n, array));
		
	}
}