import sys

# k, p, second = map(int, input().split())
#
# for i in range(second):
#     k = (k*p) % 1000000007
#
# print(k)
#

#리펙터링 소스코드
import sys

k, p, second = map(int, input().split())

for i in range(second):
    k = (k*p) % 1000000007

print(k)


#시간초과
#리펙터링 소스코드 2
k, p, second = map(int, input().split())

k = (k * (p**second)) % 1000000007

print(k)
