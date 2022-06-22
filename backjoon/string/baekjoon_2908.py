#BAEKJOON 2908
#print number
#문자열 일일이 파싱하는것보다 리스트 형식으로 받아서 reverse하는게 더 효율적..


inputNumber = list(map(str, input().split()))
reverseList =[]
for number in inputNumber:
    listStr = list(number)
    revNumber=""
    for index in reversed(range(0, len(listStr))):
        revNumber = revNumber + listStr[index]
    reverseList.append(revNumber)

maxNumber = int(reverseList[0])
if(maxNumber > int(reverseList[1])):
    print(maxNumber)
else:
    print(int(reverseList[1]))