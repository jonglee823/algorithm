package STUDY;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

//프로그래머스 LEVEL1 신고 결과 받기 
//https://programmers.co.kr/learn/courses/30/lessons/92334?language=java
//2022.06.23
/*
 * 성능개선 및 간결한 코드 작성을 위해 리펙터링..
 * 참고 : 프로그래머스 김호영님 코드
 * 테스트 21번 기존 194ms --> 110ms
 */
public class ReportResult2 {
	public static void main(String[] args) {
		String[] id_list = {"muzi", "frodo", "apeach", "neo"};
		String[] report = {"muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"};
		int k = 2;
		
		int[] answer = new int[id_list.length];
		//Arrays.fill(answer, 0);										//기본값은 0으로 초기화므로,, 필요x
		Map<String, List<String>> reportedMap = new HashMap<>();	//key:신고 당한사람 value: 신고 한사
		Set<String> rptSetMap = new HashSet<String>();					//중복제거용 Set
		Map<String, Integer> idIndex = new HashMap<>();					//배열 index 대체용 hashMap
		
		for(int i=0; i<id_list.length; i++) {
			reportedMap.put(id_list[i], new ArrayList<>());
			idIndex.put(id_list[i], i);
		}
		
		for(String temp : report) {
			rptSetMap.add(temp);
		}
		
		for(String str :rptSetMap) {
			String[] tempArray = str.split(" ");
			reportedMap.get(tempArray[1]).add(tempArray[0]);
		}
		
		for(int i=0; i<id_list.length; i++) {
			List<String> getReportdList = reportedMap.get(id_list[i]); 
			if(getReportdList.size() >= k) {
				for(String rptPerson : getReportdList) {
					int index = idIndex.get(rptPerson);
					answer[index]++;
				}
			}
		}	
	}
}