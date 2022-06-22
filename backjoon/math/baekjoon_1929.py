#baekjoon_1929
# 소수 구하기
# 소요시간 3624ms start
# import math
#
# M,N = map(int, input().split())
#
# def func(num):
#     if (num == 1):
#         return ''
#     trueYn = True
#     for x in range(2, math.trunc(math.sqrt(num)+1)):
#         if num % x == 0:
#             trueYn = False
#             break
#     if(trueYn):
#         print(num)
#
# for i in range(M, N+1):
#     func(i)
# 소요시간 3624ms end

#376ms 짜리 다른분 코드 start
#https://www.acmicpc.net/source/43395320 참고

M, N = list(map(int, input().split()))
numList = [True] * (N+1)

for i in range(2,int((N+1)**0.5)+1):
    if numList[i]:
        for j in range(i+i,N+1,i):
            numList[j]=False

answer = [i for i in range(2,N+1) if numList[i]==True]

for i in range(len(answer)):
    if answer[i]>=M:
        print(answer[i])
#376ms 짜리 다른분 코드 end