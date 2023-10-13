def solution(n, m, section):
    answer = 0

    chkList = [True] * (n + 1)
    for i in section:
        chkList[i] = False

    for index, i in enumerate(section):
        if chkList[i] == False:
            answer += 1
            

    return answer



print(solution(8, 4, [2, 3, 6]))