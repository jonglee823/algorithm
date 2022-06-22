package STUDY;

import java.util.*;

public class DivisorNumber {

	public static void main(String args[]) {
		int n = 3000;
		int answer = 0;
		for(int i=1; i<=n; i++) {
			if(n % i ==0) {
				answer += i;
				if(n / i != i) {
					answer +=(n/i);
				}
			}
		}
	}
}
