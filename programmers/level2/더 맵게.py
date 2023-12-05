from heapq import heappush, heappop

def solution(scoville, K):
    answer = 0
    h = []

    sorted(scoville)
    for i in scoville:
        heappush(h, i)

    while h[0] < K:
        a = heappop(h)
        b = heappop(h)
        c = a + (b * 2)
        heappush(h, c)
        answer += 1
        if len(h) == 1 and h[0] < K:
            return -1
    return answer