#프로그래머스 LEVEL2 다음 큰 숫자
def solution(n):
    nB = format(n, 'b')
    oneCount = str(nB).count("1")

    value = n + 1
    while True:
        valueB = format(value, 'b')
        valueBCount = str(valueB).count("1")
        if oneCount == valueBCount:
            break
        else:
            value += 1
    return value

#다른사람 리펙터리 소스코드
def solution(n):
    value = n + 1
    nCount = bin(n).count('1')
    while True:
        if nCount == bin(value).count('1'):
            break
        else:
            value += 1
    return value