#프로그래머스 LEVEL2
#할인 행사
from collections import Counter

def solution(want, number, discount):
    answer = 0
    wantDict = Counter()

    for idx, num in enumerate(number):
        wantDict[want[idx]] = num

    start, end = 0, 10
    for i in range(0, len(discount), 1):
        discDict = Counter(discount[start:end])

        if len(wantDict - discDict) == 0:
            answer += 1

        start += 1
        end += 1

    return answer