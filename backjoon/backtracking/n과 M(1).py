#BAEKJOON 백트랙킹
#N과 M(1)

import sys

def rcur(num):
    if num == M:
        print(' '.join(map(str, rs)))
        return
    for i in range(1, N+1):
        if visited[i] == False:
            visited[i] = True
            rs.append(i)
            rcur(num+1)
            rs.pop()
            visited[i] = False


input = sys.stdin.readline
N, M = map(int, input().split())
visited = [False] * (N+1)
rs = []
rcur(0)





