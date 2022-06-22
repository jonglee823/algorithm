#baekjoon 10818
#N개의 정수가 주어질때 최솟값과 최댓값을 구하는 프로그램

N = int(input())
numList = list(map(int, input().split()))
print(min(numList), max(numList))