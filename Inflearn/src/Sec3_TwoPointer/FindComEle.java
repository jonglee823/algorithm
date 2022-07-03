package Sec3_TwoPointer;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class FindComEle {
	
	public ArrayList<Integer> solution(int n, int m, int[] num1, int[] num2){
		ArrayList<Integer> answer = new ArrayList<>();
		
		Arrays.sort(num1);
		Arrays.sort(num2);
		
		int p1=0, p2=0;
		
		while(p1 < n && p2 < m) {
			
			if(num1[p1] == num2[p2]) {
				answer.add(num1[p1++]);
				p2++;
			}
			else if(num1[p1] < num2[p2]) {
				p1++;
			}else {
				p2++;
			}
		}		
		
		
		return answer;
	}

	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		FindComEle T = new FindComEle();
		
		int n = kb.nextInt();
		int[] num1 = new int[n];
		
		for(int i=0; i<n; i++) {
			num1[i] = kb.nextInt();
		}
		
		int m = kb.nextInt();
		int[] num2 = new int[m];
		
		for(int i=0; i<m; i++) {
			num2[i] = kb.nextInt();
		}
		
		for(int num : T.solution(n, m, num1, num2)) {
			System.out.print(num + " ");
		}
		
	}

}
