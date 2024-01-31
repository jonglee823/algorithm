import sys

n = int(input())
real = [list(map(int, input().split())) for _ in range(n)]

result = sorted(real, key = lambda x:x[1])[0]
print(result[0], result[1])