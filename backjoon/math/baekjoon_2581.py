#baekjoon_2581
#소수를 찾아서 소수의 합, 최솟값 구하기
import sys

M = int(input())
N = int(input())
pNumberList = [i for i in range(M,N+1)]

for i in range(M, N+1):
    if i == 1:
        pNumberList.remove(1)
        pass
    for x in range (2, i):
        if(i % x == 0):
            pNumberList.remove(i)
            break
if len(pNumberList) < 1:
    print(-1)
else:
    print(sum(pNumberList))
    print(min(pNumberList))