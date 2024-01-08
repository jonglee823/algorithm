N = int(input())
nList = list(map(int, input().split()))
M = int(input())
mList = list(map(int, input().split()))

nDict = {}

for i in nList:
    if nDict.get(i) != None:
        nDict[i] += 1
    else:
        nDict[i] = 1

for i in mList:
    if nDict.get(i) != None:
        print(nDict[i], end =' ')
    else:
        print(0, end =' ')