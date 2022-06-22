#baekjoon_11653
#소인수분해

#다른분 코드 보고 리펙터링 한 코드
#내가 짠 코드 시작
import sys
number = int(sys.stdin.readline())

def func(number):
    if number == 1:
        return ''
    for i in range(2, number+1):
        if  number % i == 0:
            print(i)
            return func(number//i)
    return number

print(func(number))


#내가 짠 코드 끝



#속도가 더 좋은 코드
# import math
#
# N = int(input())
#
# def func(num):
#     if num == 1:
#         return ''
#     print("num : " , num)
#     print("math.sqrt(num) +1 : " , math.sqrt(num) + 1)
#     print(math.trunc(math.sqrt(num)+1))
#     for i in range(2, math.trunc(math.sqrt(num)+1)):
#         if num%i == 0:
#             print(i)
#             return func(num//i)
#     return num
#
# print(func(N))
