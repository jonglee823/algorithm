#프로그래머스 LEVEL2
from collections import deque

def solution(s):
    queue = deque()

    for char in s:
        if char == "(":
            queue.append(char)
        elif queue and char == ")":
            queue.popleft()
        else:
            queue.append(char)
            break

    return len(queue) == 0