package STUDY;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class LostGymSuit {
/*
 * 프로그래머스 LEVEL 1
 * 체육
 * 2022.06.28
 * 
 */
	public static void main(String[] args) {
		int n = 3;
		int[] lost = {2}; 
		int[] reserve = {2};
		int answer = n - lost.length;
		
		Arrays.sort(lost);
		Arrays.sort(reserve);
		
		HashMap<Integer, Integer> reserveMap = new HashMap<>();
		
		for(int i =0; i<reserve.length; i++) {
			int index = Arrays.binarySearch(lost, reserve[i]); 
			System.out.println(index);
			if(index > -1) {
				lost[index] = -99;
				answer+=1;
			}else {
				reserveMap.put(i, reserve[i]);
			}
		}

		if(reserve.length > 0) {
			for(int i=0; i<lost.length; i++){
				Iterator it = reserveMap.entrySet().iterator();
				while(it.hasNext()) {
					Map.Entry map = (Map.Entry)it.next();
					if(Math.abs(lost[i] - (Integer) map.getValue()) == 1) {
						answer+=1;
						reserveMap.remove(map.getKey());
						break;
					}
				}
			}
		}
		System.out.println("answer : " + answer);
		
	}

}
