#프로그래머스 LEVEL2
#점프와 순간 이동

def solution(n):
    ans = 1

    while n >= 2:
        while n % 2 != 0:
            n -= 1
            ans += 1
        n //= 2

    return ans