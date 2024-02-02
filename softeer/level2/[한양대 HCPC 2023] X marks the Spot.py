import sys

##시간 초과 소스코드
n = int(input())
textList = [list(map(str, input().split())) for _ in range(n)]
answer = ''

for text in textList:
    s = text[0]
    p = text[1]
    answer += p[max(s.find('x'), s.find('X'))].upper()

print(answer)


#정답 코드
from collections import deque
import sys

n = int(input())
textList = [list(map(str, input().split())) for _ in range(n)]
answer = []

for text in textList:
    s = deque(text[0])
    p = deque(text[1])

    while s:
        if s[0] == 'x' or s[0] == 'X':
            answer.append(p[0].upper())
            break
        else:
            s.popleft()
            p.popleft()

for i in answer:
    print(i, end='')