#프로그래머스 LEVEL2
#두 큐 합 같게 만들기
from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    value1 = sum(queue1)
    value2 = sum(queue2)
    result = int(value1 + value2) // 2
    answer = 0

    i = 0
    que1Size = len(queue1)
    while i <= que1Size * 4:
        i += 1
        if value1 == result:
            return answer

        if value1 < result:
            value2 -= queue2[0]
            value1 += queue2[0]
            queue1.append(queue2.popleft())
            answer += 1
        else:
            value1 -= queue1[0]
            value2 += queue1[0]
            queue2.append(queue1.popleft())
            answer += 1

    else:
        return -1

    return answer