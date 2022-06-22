#baekjoon_2292
#육각형으로 이루어진 벌집이 있을때 N까지의 최소 거리
N = int(input())
value = 1
n = 0
for index in range(N):
    n += index
    value = 6 * n + 1
    if value >= N:
        print(index + 1)
        break