#프로그래머스 LEVEL2
#게임 맵 최단거리

#DFS 효율성 통과 못함
from collections import deque

answer = 99999

def dfs(maps, visited, cnt, x, y):
    global answer

    # MAP을 벗어난 경우
    if min(x, y) < 0 or x >= len(maps[0]) or y >= len(maps):
        return

    # 목적지에 도착한경우
    if x == (len(maps[0]) - 1) and y == (len(maps) - 1):
        if answer > cnt:
            answer = cnt
        return

    # 이미 방문했거나, 벽으로 막힌경우
    if visited[y][x] == True or maps[y][x] == 0:
        return

    visited[y][x] = True
    dfs(maps, visited, cnt + 1, x + 1, y)  # 우
    dfs(maps, visited, cnt + 1, x - 1, y)  # 좌
    dfs(maps, visited, cnt + 1, x, y + 1)  # 하
    dfs(maps, visited, cnt + 1, x, y - 1)  # 상
    visited[y][x] = False


def solution(maps):
    global answer
    visited = [[False for i in range(len(maps[0]))] for j in range(len(maps))]

    # 0:벽, 1:이동 가능

    dfs(maps, visited, 1, 0, 0)

    if answer == 99999:
        return -1

    return answer
