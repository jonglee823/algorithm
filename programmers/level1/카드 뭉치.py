#프로그래머스 LEVEL1
#카드 뭉치
#리펙터링 소스코드
from collections import deque


def solution(cards1, cards2, goal):
    answer = 'Yes'

    queue1 = deque(cards1)
    queue2 = deque(cards2)

    for char in goal:
        if queue1 and queue1[0] == char:
            queue1.popleft()
        elif queue2 and queue2[0] == char:
            queue2.popleft()
        else:
            answer = "No"
            break

    return answer


#처음짠 소스코드
from collections import deque
def solution(cards1, cards2, goal):
    answer = 'Yes'

    queue1 = deque(cards1)
    queue2 = deque(cards2)

    text1 = queue1.popleft()
    text2 = queue2.popleft()
    for idx in range(len(goal)):
        if text1 == goal[idx]:
            if queue1:
                text1 = queue1.popleft()
        elif text2 == goal[idx]:
            if queue2:
                text2 = queue2.popleft()
        else:
            answer = "No"
            break

    return answer

