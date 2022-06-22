package STUDY;

import java.util.*;

public class study {

	public static void main(String[] args) {
		String[] strings = {"abce", "abcd" ,"cdx"};
		int n = 2;
	      Arrays.sort(strings, new Comparator<String>(){
	          @Override
	          public int compare(String s1, String s2){
	              if(s1.charAt(n) > s2.charAt(n)) return 1;
	              else if(s1.charAt(n) == s2.charAt(n)) return s1.compareTo(s2);
	              return s1.charAt(n) - s2.charAt(n);
	          }
	      });
	      
	      for(int i=0; i<strings.length; i++) {
	    	  System.out.print(strings[i] + ", ");
	      }
	  }
}