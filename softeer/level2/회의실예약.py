import sys

# N 회의실 수
# M 예약된 회의실 수
N, M = map(int, input().split())

reservDict = {}

for i in range(N):
    name = input()
    reservDict[name] = [0] * 18 + [1]  # 빈공간일때 0, 예약일때 1

print(reservDict)

for i in range(M):
    room, startTime, endTime = input().split()
    startTime = int(startTime)
    endTime = int(endTime)
    for j in range(startTime, endTime):
        reservDict[room][j] = 1

reservDict = dict(sorted(reservDict.items()))

for idx, room in enumerate(reservDict):
    current = 1
    temp = []
    for j in range(9, 19):
        if current == 1 and reservDict[room][j] == 0:
            sTime = j
            current = 0
        elif current == 0 and reservDict[room][j] == 1:
            fTime = j
            current = 1
            temp.append([sTime, fTime])

    # if current ==0:
    # temp.append([sTime, 18])

    print('Room ' + room + ':')
    if len(temp) == 0:
        print('Not available')
    else:
        print(len(temp), 'available:')
        for x in range(len(temp)):
            print(f'{temp[x][0]:02d}-{temp[x][1]}')
    if idx < N - 1:
        print('-----')

# print(reservDict)