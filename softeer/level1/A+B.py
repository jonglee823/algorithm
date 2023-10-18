import sys

n = int(input())

for idx in range(n):
    a, b = map(int, input().split())
    print("Case #"+str(idx+1)+": "+str(a+b))