package Sec3_TwoPointer;

import java.util.Scanner;
import java.util.ArrayList;
public class MergeTwoArray {
	
	public ArrayList<Integer> solution(int[] num1, int[] num2) {
		ArrayList answer = new ArrayList<>();
		
		int p1 = 0, p2=0;
		int i=0;
		while(p1 <num1.length && p2<num2.length) {
			if(num1[p1] < num2[p2]) {
				answer.add(num1[p1++]);
			}else {
				answer.add(num2[p2++]);
			}
		}
		
		while(p1<num1.length) answer.add(num1[p1++]);
		while(p2<num2.length) answer.add(num2[p2++]);
		
		return answer;
	}

	public static void main(String[] args) {
		Scanner kb = new Scanner(System.in);
		MergeTwoArray T = new MergeTwoArray();
		
		int case1 = kb.nextInt();
		int[] num1 = new int[case1];
		for(int i=0; i<case1; i++) {
			num1[i] = kb.nextInt();
		}
		
		
		int case2 = kb.nextInt();
		int[] num2 = new int[case2];
		for(int i=0; i<case2; i++) {
			num2[i] = kb.nextInt();
		}		
		
		for(int x : T.solution(num1, num2)) {
			System.out.print(x + " ");
		}
	}

}
