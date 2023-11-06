#프로그래머스 LEVEL2
#Bottom-UP
def solution(n):
    d = [0] * (n + 1)
    d[1] = 1
    d[2] = 1
    for i in range(3, n + 1):
        d[i] = d[i - 1] + d[i - 2]

    return d[n] % 1234567
