#Softeer 근무시간
import sys

result = 0
timeList = list(input().split() for _ in range(5))

for time in timeList:
    starthr, startMi = map(int, time[0].split(':'))
    endhr, endMi = map(int, time[1].split(':'))

    if endMi < startMi:
        endMi += 60
        endhr -= 1

    # hour
    result = result + ((endhr - starthr) * 60) + (endMi - startMi)

print(result)