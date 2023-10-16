#2023-10-16
#프로그래머스 LVEVL1
def solution(a, b, n):
    answer = 0

    while True:

        if n < a:
            break

        payback = (n // a)
        answer += (payback * b)
        n = (payback * b) + (n % a)
        print('n : ', n, ' answer : ', answer)
    return answer

#리펙터링 코드
def solution(a, b, n):
    answer = 0

    while n >= a:
        answer += ((n // a) * b)
        n = (((n // a)) * b) + (n % a)
    return answer