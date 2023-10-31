#Softeer LEVEL3
#지자동차 테스트
#2023-10-26

import sys
from itertools import combinations

n, q = map(int, input().split())

valueList = sorted(list(map(int, input().split())))
MiList =[list(map(int, input())) for _ in range(q)]

setMi=list(combinations(valueList, 3))

for i in range(len(MiList)):
    result = 0
    for value in setMi:
        if value[1] == MiList[i][0]:
            result += 1
    print(result)


#리펙터링 소스코드
import sys
from sys import stdin, stdout
import bisect

input = stdin.readline
#print = stdout.write

n, q = map(int, input().split())

mpg_values = sorted(list(map(int, input().split())))

for _ in range(q):
    m = int(input())
    idx = bisect.bisect_left(mpg_values, m)
    if idx != n and m == mpg_values[idx]:
        print(idx*(n-idx-1))
    else:
        print(0)