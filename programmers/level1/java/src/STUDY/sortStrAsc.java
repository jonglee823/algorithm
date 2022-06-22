package STUDY;

import java.util.*;

public class sortStrAsc {

	public static void main(String[] args) {
		String s = "Zbcdefg";
		String[] array = s.split("");
		
		Arrays.sort(array, Collections.reverseOrder());
		 System.out.print(String.join("", array));

	}

}
