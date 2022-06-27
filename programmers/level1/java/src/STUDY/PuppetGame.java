package STUDY;

import java.util.Stack;

/*프로그래머스 LEVEL1 크레인 인형뽑기 Game
 * 2022.06.27
 */
public class PuppetGame {
	
	static Stack<Integer> stack = new Stack<>();

	public static void main(String[] args) {
		int[][] board = {{0,0,0,0,0},{0,0,1,0,3},{0,2,5,0,1},{4,2,4,4,2},{3,5,1,3,1}};
		int[] moves = {1,5,3,5,1,2,1,4};
		int answer = 0;
		
		for(int i=0; i<moves.length; i++) {
			for(int x=0; x<board.length; x++) {
				if(board[x][moves[i]-1] != 0) {			
					answer += pushStack(stack, board[x][moves[i]-1]);
					board[x][moves[i]-1] = 0;
					break;
				}
			}
		}

		System.out.println(answer);
	}
	
	public static Integer pushStack(Stack<Integer> stack, int value) {
		int count = 0;
		
		if(stack.isEmpty()) {
			stack.push(value);
			return 0;
		}else {
			if(value == stack.peek()) {
				stack.pop();
				count +=2;
			}else{
				stack.push(value);
			}
		}
		return count;
	}	
}