#리펙터링 소스코드(프로그래머스 faul2chris님 답안)
def solution(park, routes):
    W = len(park[0])
    park = [['X']*(W+2)] + [[*'X'+i+'X'] for i in park] + [['X']*(W+2)]

    # 시작위치 가져오기
    for i, rot in enumerate(park):
        if "S" in rot:
            answer = [i, rot.index("S")]

    move = {k : v for k, v in zip('NEWS', [(-1, 0), (0, 1), (0, -1), (1, 0)])}

    x,y = answer[0], answer[1]
    for route in routes:
        op, n = route.split()
        for k in range(1, int(n) + 1):
            X, Y = x+k*move[op][0], y+k*move[op][1]
            if park[X][Y] == 'X':
                break
        else:
            x, y = X,Y

    return [x-1, y-1]

#내가 작성한 답안 코드
# def solution(park, routes):
#     answer = []
#     W = len(park[0])  # 가로
#     H = len(park)  # 세로
#
#     # 시작위치 가져오기
#     for i, rot in enumerate(park):
#         if rot.find("S") != -1:
#             answer = [i, rot.find("S")]
#     # print('start answer :',answer)
#
#     mveVal = {'N': [-1, 0], 'S': [1, 0], 'E': [0, 1], 'W': [0, -1]}
#     for strVal in routes:
#         checkTF = True
#         op, n = strVal.split()
#         n = int(n)
#         # 공원벗어나는경우 명령 무시
#         chk = [x + y for x, y in zip(answer, (mveVal[op][0] * n, mveVal[op][1] * n))]
#         # print('chk : ', chk, ' mveVal[op][0] : ', mveVal[op][0], ' mveVal[op][1] : ',mveVal[op][1])
#         if chk[0] < 0 or chk[0] >= H or chk[1] < 0 or chk[1] >= W:
#             checkTF = False
#             continue
#         # 이동경로에 장애물이 있는지 체크
#
#         # W,E 이동
#         if op == 'E' and park[answer[0]][answer[1]:chk[1] + 1].find("X") != -1:
#             checkTF = False
#             continue
#         if op == 'W' and park[answer[0]][chk[1]:answer[1]].find("X") != -1:
#             checkTF = False
#             continue
#
#         # N,S 이동
#         for i in range(n + 1):
#             if op == 'S' and park[answer[0] + i][answer[1]].find("X") != -1:
#                 checkTF = False
#                 break
#             if op == 'N' and park[answer[0] - i][answer[1]].find("X") != -1:
#                 checkTF = False
#                 break
#         if checkTF == True:
#             answer = chk
#     return answer

