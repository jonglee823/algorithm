#프로그래머스 LEVEL2
#피로도


#순열을 이용한 완전 탐색
# from itertools import permutations
#
# def solution(k, dungeons):
#     answer = 0
#     for p in permutations(dungeons, len(dungeons)):
#         tmp = k
#         cnt = 0
#         for need, spend in p:
#             if tmp >= need:
#                 tmp -= spend
#                 cnt += 1
#         answer = max(answer, cnt)
#
#     return answer


#백트래킹을 이용한 방법

answer = 0

def dfs(k, dungeons, visited, cnt):
    global answer

    if cnt > answer:
        answer = cnt

    for idx, dungeon in enumerate(dungeons):
        if not visited[idx] and k >= dungeon[0]:
            visited[idx] = True
            dfs(k - dungeon[1], dungeons, visited, cnt + 1)
            visited[idx] = False


def solution(k, dungeons):
    global answer
    visited = [False] * len(dungeons)
    dfs(k, dungeons, visited, 0)

    return answer