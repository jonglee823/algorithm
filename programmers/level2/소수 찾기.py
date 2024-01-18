#프로그래머스 LEVEL2
#소수 찾기
from itertools import permutations
import math
def findPrimeNumber(tempList):
    n = max(tempList)
    DP = [False, False] + [True] * n

    for i in range(2, n + 1):
        if DP[i] == True:
            j = 2
            while i * j <= n:
                DP[i * j] = False
                j += 1
    return DP

def solution(numbers):
    answer = 0

    tempSet = []

    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers, i):
            if int(''.join(j)) == 0:
                continue
            tempSet.append(int(''.join(j)))

    tempSet = list(set(tempSet))
    temp = findPrimeNumber(tempSet)
    for i in tempSet:
        if temp[i] == True:
            print(i)
            answer += 1

    return answer

