import sys

global answer

def checkLand(array):
    cnt = 0
    if len(set(array)) == 1:
        return 0
    else:
        array.sort()
        cnt += abs(array[1]-array[0]) + abs(array[2] - array[1])
        return cnt


land = [list(map(int, input().split())) for _ in range(3)]
revLand = [[0] * 3 for _ in range(3)]

answer = 10000

for i in range(3):
    for j in range(3):
        revLand[i][j] = land[j][i]

for i in land:
    answer = min(checkLand(i), answer)

for i in revLand:
    answer = min(checkLand(i), answer)

print(answer)