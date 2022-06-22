#baekjoon_10250
#ACM hotel

#H : hotel 층수
#W : 층의 방 수
#N : 몇 번째 손님

T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]

for numList in arr:
    height = (numList[2] % numList[0])
    widthNum = (numList[2] // numList[0])

    if(numList[2] % numList[0] == 0):
        height = numList[0]

    if(numList[2] % numList[0] >= 1):
        widthNum +=1

    print(str(height)+str(widthNum).zfill(2))

