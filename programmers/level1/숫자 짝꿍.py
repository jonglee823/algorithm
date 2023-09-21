def solution(X, Y):
    answer = ''
    xDic = {}
    yDic = {}

    for idx, i in enumerate(X):
        if i not in xDic:
            xDic[i] = 1
        else:
            xDic[i] = xDic[i] + 1

    for idx, i in enumerate(Y):
        if i not in yDic:
            yDic[i] = 1
        else:
            yDic[i] = yDic[i] + 1
    for i in range(9, -1, -1):
        if str(i) in xDic and str(i) in yDic:
            for x in range(min(xDic[str(i)], yDic[str(i)])):
                if answer == '' and i == 0:
                    answer += str(i)
                    break
                else:
                    answer += str(i)
    if answer == '':
        answer = '-1'
    return answer