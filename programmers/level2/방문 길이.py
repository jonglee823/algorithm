#프로그래머스 LEVEL2
#방문길이

def solution(dirs):
    answer = 0
    nx = 5
    ny = 5

    moveDic = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    reverseDic = {"U": "D", "D": "U", "L": "R", "R": "L"}
    checkDic = {}

    for move in dirs:
        x, y = moveDic[move]

        if min(nx + x, ny + y) < 0 or max(nx + x, ny + y) > 10:
            continue

        nx += x
        ny += y
        check = move + str(nx) + str(ny)
        check2 = reverseDic[move] + str(nx - x) + str(ny - y)

        if check not in checkDic and check2 not in checkDic:
            answer += 1
            checkDic[check] = 0
            checkDic[check2] = 0

    return answer