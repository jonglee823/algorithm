from collections import defaultdict
import math


def solution(fees, records):
    answer = defaultdict(int)
    inDict = {}

    for x in records:
        clock, carNum, gubun = map(str, x.split())
        hour, minut = map(int, clock.split(':'))
        time = (hour * 60) + minut

        if gubun == 'IN':
            inDict[carNum] = time
        else:
            parkingTime = time - inDict[carNum]
            answer[carNum] += parkingTime
            del inDict[carNum]

    for carNum, time in inDict.items():
        parkingTime = (23 * 60) + 59 - time
        answer[carNum] += parkingTime

    result = []

    for carNum, time in sorted(answer.items()):
        if time < fees[0]:
            result.append(fees[1])
        else:
            parkingFee = fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3]
            result.append(parkingFee)

    return result