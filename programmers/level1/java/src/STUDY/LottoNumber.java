package STUDY;

import java.util.HashMap;
import java.util.Map;

//프로그래머스 LEVEL1 로또의 최고 순위와 최저 순
public class LottoNumber {

	public static void main(String[] args) {
		int[] lottos = {44, 1, 0, 0, 31, 25};
		int[] win_nums = {31, 10, 45, 1, 6, 19};
        Map<Integer, Boolean> map = new HashMap<Integer, Boolean>();
        int zeroCount = 0;

        for(int lotto : lottos) {
            if(lotto == 0) {
                zeroCount++;
                continue;
            }
            map.put(lotto, true);
        }

        int sameCount = 0;
        for(int winNum : win_nums) {
            if(map.get(winNum) != null) sameCount++;
        }

        int maxRank = 7 - (sameCount + zeroCount);
        int minRank = 7 - sameCount;
        
        if(minRank > 6) minRank = 6;
        if(maxRank > 6) maxRank = 6;

        //return new int[] {maxRank, minRank};
    }
}