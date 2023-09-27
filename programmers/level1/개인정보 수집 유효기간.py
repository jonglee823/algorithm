def solution(today, terms, privacies):
    answer = []
    todayYYYY, todayMM, todayDD = map(int, today.split('.'))
    dayCount = ((todayYYYY - 1) * 12 * 28) + ((todayMM - 1) * 28) + todayDD

    terDic = {}

    # 약관 DD값으로 초기화
    for term in terms:
        a, b = term.split()
        b = int(b)
        terDic[a] = b * 28

    for idx, privac in enumerate(privacies):
        yyymmdd, term = privac.split()
        privYYYY, privMM, privDD = map(int, yyymmdd.split('.'))
        privDayCount = ((privYYYY - 1) * 12 * 28) + ((privMM - 1) * 28) + privDD

        if privDayCount + terDic[term] <= dayCount:
            answer.append(idx + 1)

    return answer