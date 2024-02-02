import sys

n = int(input())
home = list(map(int, input().split()))
length = (max(home) + 1)
answer = [0] * length
home.sort()

for z in range(2, length):
    cnt = 0
    for i in home:
        if i % z == 0:
            cnt += 1
    answer[z] = cnt

print(max(answer))
