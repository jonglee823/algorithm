#2562 최댓값 찾기

numberList = list(int(input()) for _ in range(9))

print(max(numberList))
print(numberList.index(max(numberList))+1)