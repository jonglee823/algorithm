#금고털이 내가 짠 코드
#소스코드 문제점. 가격이 같은 값이 들어올경우 덮어써짐. 따라서 리스트에 튜플 사용 필요
import sys

w, n = map(int, input().split())

jewelList = [0] * ((10**4)+1)
result = 0
for i in range(n):
    m, p = map(int, input().split())
    jewelList[p] = m

for i in range(len(jewelList)-1, 0, -1):
    if jewelList[i] == 0:
       continue
    if w - jewelList[i] > 0:
        result += (jewelList[i] * i )
        w -= jewelList[i]
    elif w >= 0:
        result += (w * i)
        break

print(result)


#이게 되네..?
import sys
input = sys.stdin.readline

w, n = map(int,input().split())

valueInfo = [list(map(int,input().split())) for _ in range(n)]
valueInfo.sort(key = lambda x : x[1], reverse = True)

result = 0
for m, p in valueInfo:
    if w - m >= 0:
        w -= m
        result += (m*p)
    else:
        result += (w*p)
        break

print(result)