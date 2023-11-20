#프로그래머스 LEVEL2
#기능 개발
def solution(progresses, speeds):
    answer = []
    jobList = []

    for idx in range(len(progresses)):
        day = (100 - progresses[idx]) // speeds[idx]
        if (100 - progresses[idx]) % speeds[idx] != 0: day += 1
        jobList.append(day)

    checkVal = jobList[0]
    count = 1

    for idx in range(1, len(jobList)):
        if checkVal >= jobList[idx]:
            count += 1
        else:
            answer.append(count)
            count = 1
            checkVal = jobList[idx]
    answer.append(count)

    return answer