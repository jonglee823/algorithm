#start 2023 10 04

from itertools import combinations

def solution(number):
    answer = 0
    numList = list(combinations(number, 3))

    for num in numList:
        if sum(num) == 0:
            answer +=1
    return answer