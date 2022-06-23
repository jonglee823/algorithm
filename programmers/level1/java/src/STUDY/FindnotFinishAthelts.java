package STUDY;

import java.util.HashMap;
import java.util.Map;

/*
 * 프로그래머스 LEVEL1 완주하지 못한 선수
 * https://programmers.co.kr/learn/courses/30/lessons/42576
 * 2022.06.23
 * jh2@kakao.com
 */
public class FindnotFinishAthelts {

	public static void main(String[] args) {
		String[] participant = {"mislav", "stanko", "mislav", "ana"};
		String[] completion = {"stanko", "ana", "mislav"};
		Map<String, Integer> hashMap = new HashMap<>();
		
		for(String particName : participant) {
			hashMap.put(particName, hashMap.getOrDefault(particName, 0) +1);		//map.getOrDefault --> 값이 있을경우 해당 값리턴 / 없으면 default value
		}
				
		//개선 전 코드 start 
//		for(String particName : participant) {
//			if(hashMap.get(particName) != null) {
//				hashMap.put(particName, hashMap.get(particName)+1);
//			}else {
//				hashMap.put(particName, 1);
//			}	
//		}
		//개선 전 코드 end
		
		System.out.println("participant Name : " + hashMap.toString());
		
		for(String compName : completion) {
			int count = hashMap.get(compName);
			if(count > 1) {
				hashMap.put(compName, --count);
			}else {
				hashMap.remove(compName);
			}
		}
		//System.out.println("compName Name : " + hashMap.toString());
		
		for(String name : hashMap.keySet()) {
			System.out.println(name);
		}
		
		
		
		//System.out.println(hashMap.entrySet().iterator().next().getKey());
		//return hashMap.entrySet().iterator().next().getKey();
	}
}