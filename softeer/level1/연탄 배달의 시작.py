import sys

resultDic = {}

n = int(input())
array = list(map(int, input().split()))

for i in range(len(array)-1):
    temp = abs(array[i] - array[i+1])
    if temp in resultDic:
        resultDic[temp] += 1
    else:
        resultDic[temp] = 1

print(resultDic[min(resultDic.keys())])