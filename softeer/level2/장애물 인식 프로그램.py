#장애물 인식 프로그램
#Softeer Level2

#https://fre2-dom.tistory.com/24 출처

#BFS
from collections import deque

n = int(input())
array = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
result = []


def bfs(x, y):
    queue = deque([(x, y)])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    cnt = 0
    while queue:
        cx, cy = queue.popleft()
        if 0 <= cx < n and 0 <= cy < n and not visited[cx][cy] and array[cx][cy] == 1:
            visited[cx][cy] = True
            cnt += 1
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                queue.append((nx, ny))
    return cnt


for i in range(n):
    for j in range(n):
        if not visited[i][j] and array[i][j] == 1:
            result.append(bfs(i, j))

print(len(result))
result.sort()
for i in result:
    print(i)


import sys

def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return True

    if graph[x][y] == 1:
        cnt.append(1)
        graph[x][y] = 2
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


N = int(input())

graph = []

for i in range(N):
    graph.append(list(map(int, input())))

cnt = []
result = 0
resultList = []
for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            result += 1
            resultList.append(len(cnt))
            cnt = []

resultList.sort()
print(result)
for i in resultList:
    print(i)