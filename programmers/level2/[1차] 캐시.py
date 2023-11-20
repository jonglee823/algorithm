#프로그래머스 LEVEL2
#캐시

def solution(cacheSize, cities):
    answer = 0

    cacheList = []

    for i in range(len(cities)):
        if cities[i].upper() in cacheList:
            answer += 1
            cacheList.remove(cities[i].upper())
        else:
            answer += 5

        cacheList.append(cities[i].upper())

        if len(cacheList) > cacheSize:
            cacheList = cacheList[1::]

    return answer



#리펙터링 소스코드
from collections import deque


def solution(cacheSize, cities):
    answer = 0

    queue = deque(maxlen=cacheSize)

    for i in range(len(cities)):
        if cities[i].upper() in queue:
            answer += 1
            queue.remove(cities[i].upper())
        else:
            answer += 5

        queue.append(cities[i].upper())

    return answer