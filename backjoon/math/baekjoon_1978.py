#baekjoon_1978
#소수 찾기

t = int(input())
numList = list(map(int, input().split()))
count=t

for num in numList:
    if num ==1:
        count-=1
        pass
    for index in range(2, num):
        if num % index == 0:
            count-=1
            break
print(count)