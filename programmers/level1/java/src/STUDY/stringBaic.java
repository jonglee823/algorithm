package STUDY;

import java.util.Arrays;

public class stringBaic {
	public static void main(String args[]) {
		int[] array = {1, 5, 2, 6, 3, 7, 4};
		int[][] commands = {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};
        int[] answer = new int[commands.length];
        
        stringBaic stringBaic = new stringBaic();
        
        for(int index=0; index<commands.length; index++){
           int[] tmepArray = stringBaic.getSlice(array, commands[index][0]-1, commands[index][1]);
           answer[index] = tmepArray[commands[index][2]];
        }
        
        System.out.print(Arrays.toString(answer));
    }
    
    public int[] getSlice(int[] array, int start, int end){
        int[] sliceArray = new int[end - start +1];
        
        for(int i = 0; i< end-start; i++){
            sliceArray[i] = array[i+start];
        }
        
        Arrays.sort(sliceArray);
        return sliceArray;
    }

}
