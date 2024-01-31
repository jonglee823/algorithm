import sys
#https://softeer.ai/app/assessment/index.html?xid=78013&xsrfToken=oKTK3rzfpV6sUgzG5oU9iLh0KIXwB8pO&testType=practice
# d 거리
# a 뒤돌아 보는 시간
# b 앞에보는 시간

a, b, d = map(int, input().split())
answer = 0

if d % a == 0:
    answer += (d // a) * (a + b) + (d % a) - b
else:
    answer += (d // a) * (a + b) + (d % a)

answer += (d // b) * (a + b) + (d % b)  # 30 + 1
print(answer)
