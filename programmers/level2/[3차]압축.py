#프로그래머스 [3차]압축

from collections import deque


def solution(msg):
    print(ord('A'))
    queue = deque(msg)
    answer = []
    length = len(msg)

    # 알파벳 사전 초기화
    wordDic = dict([(chr(i + 65), i + 1) for i in range(26)])

    while queue:
        a = queue.popleft()

        while queue:
            if a + queue[0] in wordDic:
                a = a + queue.popleft()
            else:
                answer.append(wordDic[a])
                wordDic[a + queue[0]] = len(wordDic) + 1
                break
        else:
            answer.append(wordDic[a])

    return answer
