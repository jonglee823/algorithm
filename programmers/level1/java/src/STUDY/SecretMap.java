package STUDY;

import java.util.Arrays;

public class SecretMap {

	public static void main(String[] args) {
		int n =5;
		int[] arr1 = {9, 20, 28, 18, 11};
		int[] arr2 = {30, 1, 21, 17, 28};
		String[] answer = new String[n];
		
		for(int i=0; i<n; i++) {
			//String.format이 느림..
			//stringBuffer.append(String.format("%0"+n+"d", Integer.parseInt(Integer.toBinaryString(arr1[i] | arr2[i]))).replace(1+"", "#").replace(0+"", " "));
			String str = Integer.toBinaryString(arr1[i] | arr2[i]);
			str = String.format("%16s",str);
			System.out.println("str : " + str);
			str = str.replaceAll("1", "#");
			str = str.replaceAll("0", " ");
			answer[i] = str;
		}
		
		
		System.out.println(Arrays.toString(answer));
		//return answer;
	}

}
