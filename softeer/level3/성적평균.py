#성적평균
import sys

N, K = map(int, input().split())
scoreList = list(map(int, input().split()))

for i in range(K):
    start, end = map(int, input().split())
    print("{:.2f}".format(sum(scoreList[start-1:end])/(end-start+1)))