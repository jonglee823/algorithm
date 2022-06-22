package STUDY;

import java.util.ArrayList;
import java.util.List;

public class removeEqulNumber {

	public static void main(String[] args) {
		int[] arr= {1,1,3,3,0,1,1};
		List<Integer> numberList = new ArrayList<>();
		numberList.add(arr[0]);
		
		for(int i=1; i<arr.length; i++) {
			if(arr[i] == numberList.get(numberList.size()-1)) {
				continue;
			}else {
				numberList.add(arr[i]);
			}
		}
		System.out.print(numberList.toString());
	}

}
