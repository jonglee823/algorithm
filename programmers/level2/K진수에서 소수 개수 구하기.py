# 소수 체크
def prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# K 진법 변환
def change(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]


def solution(n, k):
    answer = 0
    number = change(n, k)
    word = number.split("0")

    for w in word:
        if len(w) == 0 or int(w) < 2:
            continue

        result = prime(int(w))

        if result:
            answer += 1

    return answer