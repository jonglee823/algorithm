#2023-10-16 프로그래머스 LEVEL 1

def solution(number, limit, power):
    answer = 0
    divdeList = []

    for i in range(1, (number + 1)):
        divdeList.append(getMyDivisor(i))

    for i in divdeList:
        if i <= limit:
            answer += i
        else:
            answer += power
    return answer


def getMyDivisor(n):
    divNumList = []

    for i in range(1, int(n ** (1 / 2)) + 1):
        if (n % i == 0):
            divNumList.append(i)
            if ((i ** 2) != n):
                divNumList.append(n // i)

    return len(divNumList)

#리펙터링 소스코드
# 2023-10-16 프로그래머스 LEVEL 1

def solution(number, limit, power):
    answer = 0

    for i in range(1, (number + 1)):
        value = getMyDivisor(i)    # 불필요 for문 제거
        if value <= limit:
            answer += value
        else:
            answer += power

    return answer


def getMyDivisor(n):
    divNumList = []

    for i in range(1, int(n ** 0.5) + 1):
        if (n % i == 0):
            divNumList.append(i)
            divNumList.append(n // i)       #조건문 제거

    return len(set(divNumList)) #Set 함수 사용하여 중복제거