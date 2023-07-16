#baekjoon 10807

numCount = int(input())
numArray = map(int, input().split())
findNum = int(input())

i = 0

for x in numArray:
    if findNum == x:
        i+=1

print(i)
