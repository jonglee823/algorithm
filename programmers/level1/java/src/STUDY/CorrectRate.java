package STUDY;

import java.util.ArrayList;

public class CorrectRate {

	//프로그래머스 수포자 정답률 
	public static void main(String[] args) {
        int[] answer = {};
        int[] person1 = {1,2,3,4,5}; //5
        int[] person2 = {2,1,2,3,2,4,2,5}; // 8
        int[] person3 = {3,3,1,1,2,2,4,4,5,5}; //10
        int answer1=0, answer2 =0, answer3 =0;
        int[] answers = {1,2,3,4,5};
        
        for(int i =0; i<answers.length; i++){
            if(person1[i % person1.length] == answers[i]) answer1++;
            if(person2[i % person2.length] == answers[i]) answer2++;
            if(person3[i % person3.length] == answers[i]) answer3++;
        }
        int max = Math.max(Math.max(answer1, answer2),answer3); // max값 구하기
        ArrayList<Integer> list = new ArrayList<Integer>();
        if(max==answer1) list.add(1); //max값이랑 같으면 넣는다.
        if(max==answer2) list.add(2);
        if(max==answer3) list.add(3);
        
        answer = new int[list.size()];
        
        for(int i =0; i<answer.length; i++) {
        	answer[i] = list.get(i);
        }
		
	}

}
