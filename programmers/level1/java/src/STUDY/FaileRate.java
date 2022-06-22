package STUDY;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class FaileRate {
	public static void main(String args[]) {
	
		int N= 5;
		int[] lastStages = {2, 1, 2, 6, 2, 4, 3, 3};
		int[] nStagePlayers = new int[N+2];
		for(int stage : lastStages) {
			nStagePlayers[stage]+= 1;
		}
		
		int remainingPlayers = lastStages.length;
		List<Stage> stageList = new ArrayList<>();
		
		for(int id=1; id<=N; id++) {
			double failure = (double) nStagePlayers[id]/ remainingPlayers;
			remainingPlayers -= nStagePlayers[id];
			
			Stage s = new Stage(id, failure);
			stageList.add(s);
		}
		
		Collections.sort(stageList, Collections.reverseOrder());
		
		int[] answer = new int[N];
		for(int i=0; i<N; i++) {
			answer[i] = stageList.get(i).getId();
		}
		
		System.out.println(Arrays.toString(answer));
	}
}


class Stage implements Comparable<Stage> {
	private int id;
	private double failure;

	Stage(int id, double failure){
		this.id = id;
		this.failure = failure;
	}
	
	

	public int getId() {
		return id;
	}



	public void setId(int id) {
		this.id = id;
	}



	public double getFailure() {
		return failure;
	}



	public void setFailure(double failure) {
		this.failure = failure;
	}



	@Override
	public int compareTo(Stage o) {
		if(failure < o.failure) {
			return -1;
		}
		if(failure > o.failure) {
			return 1;
		}
		return 0;
	}
	
}