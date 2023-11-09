#프로그래머스 n^2 배열 자르기
#시간 초과뜨는 소스코드
def solution(n, left, right):
    array = [[0 for j in range(n)] for i in range(n)]
    array_line = [0 for j in range(n * n)]

    # 2차원 배열 생성
    for i in range(n):
        for x in range(i + 1):
            array[i][x] = i + 1
            array[x][i] = i + 1

    for i in range(n * n):
        array_line[i] = array[i // n][i % n]

    return array_line[left:right + 1]

#리펙터링 소스코드
def solution(n, left, right):
    array_line = []

    for i in range(left, right + 1):
        row = i // n
        col = i % n
        max_value = max(row, col)
        array_line.append(max_value + 1)

    return array_line
