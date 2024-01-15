#[PCCE기출문제] 10번/ 데이터 분석
def solution(data, ext, val_ext, sort_by):
    # 기준으로 데이터를 뽑아낼지를 의미 ext
    # 뽑아낼 정보의 기준값 val_ext
    # 정보를 정렬할 기준이 되는 문자열 sort_by
    answer = []
    extDict = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    check = extDict[ext]

    for d in data:
        if d[check] < val_ext:
            answer.append(d)

    return sorted(answer, key=lambda d: d[extDict[sort_by]])