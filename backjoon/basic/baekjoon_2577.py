#baekjoon 2577

inputList = list(int(input()) for _ in range(3))
numberList = [0,1,2,3,4,5,6,7,8,9]

dictNumber = {numberList : 0 for numberList in numberList}

mutlpue = inputList[0] * inputList[1] * inputList[2]

for i in str(mutlpue):
    dictNumber[int(i)] += 1

for key, value in dictNumber.items():
    print(value)