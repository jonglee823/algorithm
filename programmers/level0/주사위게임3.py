# 주사위 게임3
def solution(a, b, c, d):
    answer = 0
    keyValue = {}
    valKeyDic = {}

    for i in (a, b, c, d):
        if keyValue.get(i) == None:
            keyValue[i] = 1
        else:
            keyValue[i] = keyValue[i] + 1

    for key, value in keyValue.items():
        if valKeyDic.get(value) != None:
            valKeyDic.get(value).append(key)
        else:
            valKeyDic[value] = [key]
    print('valKeyDic : ', valKeyDic)

    if len(keyValue) == 1:  # 4개 다 같은 숫자
        answer = 1111 * a
    elif len(keyValue) == 2:
        if valKeyDic.get(3) != None:  # 3개 같은숫자
            p = valKeyDic[3][0]
            q = valKeyDic[1][0]
            answer = (10 * p + q) * (10 * p + q)
        elif valKeyDic.get(2) != None:  # 2개, 2개 같은 숫자
            p = valKeyDic[2][0]
            q = valKeyDic[2][1]
            answer = (p + q) * abs(p - q)
    elif len(keyValue) == 3:
        q = valKeyDic[1][0]
        r = valKeyDic[1][1]
        answer = q * r
    elif len(keyValue) == 4:  # 4개 다 다른경우
        answer = min(a, b, c, d)
    return answer