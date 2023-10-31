#장애물 인식 프로그램
#Softeer Level2

#https://fre2-dom.tistory.com/24 출처

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