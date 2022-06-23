package STUDY;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

//프로그래머스 LEVEL1 신고 결과 받
//https://programmers.co.kr/learn/courses/30/lessons/92334?language=java
//2022.06.23
/*
 * String[] report를 HashSet 자료형으로 중복 제거
 * HashSet<String, List> 로 key 값에 신고 당한 사람의 ID, List는 신고한 사람을 insert 
 * HashSet를 순회하면서 List의 길이가 이상인사람을 insert  
 */
public class ReportResult {

	public static void main(String[] args) {
		String[] id_list = {"muzi", "frodo", "apeach", "neo"};
		String[] report = {"muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"};
		int k = 2;
		
		int[] answer = new int[id_list.length];
		Arrays.fill(answer, 0);
		HashMap<String, List<String>> hashMap = new HashMap<>();
		

		
		Set<String> repotedMap = new HashSet<String>();
		for(String str : report) {
			repotedMap.add(str);
		}
		
		for(String str :repotedMap) {
			String[] strArray = str.split(" ");
			List<String> resultList = hashMap.get(strArray[1]); 
			if(resultList != null) {
				resultList.add(strArray[0]);
				hashMap.put(strArray[1], resultList);
			}else {
				hashMap.put(strArray[1], new ArrayList<>(Arrays.asList(strArray[0])));
			}
		}
		
		for(int i=0; i<id_list.length; i++) {
			List<String> getReportdList = hashMap.get(id_list[i]); 
			if(null != getReportdList && getReportdList.size() >= k) {
				for(String rptPerson : getReportdList) {
					int index = Arrays.asList(id_list).indexOf(rptPerson);
					answer[index] = answer[index] +1;
				}
			}
		}	

	}

}
