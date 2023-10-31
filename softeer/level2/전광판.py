#내가짠 소스코드
#생각을 잘못했음.. CASE 1은 1끼리, 2는 2끼리 생각했어야함..

import sys

graph=[
    [], #0
    [(1,3),(3,5)], #1
    [(0,1), (1,3), (2, 3), (2,4), (4,5)], #2
    [(0,1), (1,3), (2,3), (3,5), (4,5)], #3
    [(0,2), (2,3), (1,3), (3,5) ], #4
    [(0,1), (0,2), (2,3), (3,5), (4,5)], #5
    [(0, 2), (2,4), (2,3), (3,5), (4,5)], #6
    [(0,1), (0,2), (1,3), (3,5)], #7
    [(0,1),(0,2),(1,3),(2,3),(2,4),(3,5),(4,5)], #8
    [(0, 1), (0,2), (1,3), (2,3), (3,5), (4,5)] #9
]
beforeA = '00000'
beforeB = '00000'

#교집합
#print(list(set(graph[1]) & set(graph[2])))

#차집합
#print(list(set(graph[1]) - set(graph[2])))


def pushSwith(beforeNumber, number):
    number = number.zfill(5)
    result = 0

    for x in range(4, -1, -1):
        pushCount = 0
        befor = int(beforeA[x])
        now = int(number[x])

        if now == 0 and befor == 0:
            continue
        pushCount += (len(list(set(graph[now]) - set(graph[befor])))//2) #켜야하는 숫자자
        pushCount -= (len(list(set(graph[befor]) & set(graph[now])))//2) #이미 그전 숫자에 켜져있는경우
        pushCount += (len(list(set(graph[befor]) - set(graph[now])))//2) #꺼야하는 숫자
        result += pushCount
    return result

T = int(input())

for i in range(T):
    A, B = map(str, input().split())
    answer = 0
    answer += pushSwith(beforeA, A)
    answer += pushSwith(beforeB, B)

    beforeA = A.zfill(5)
    beforeB = B.zfill(5)
    print(answer)


#강의듣고 짠 코드
import sys

light = {
    '0': '1110111',
    '1': '0010010',
    '2': '1011101',
    '3': '1011011',
    '4': '0111010',
    '5': '1101011',
    '6': '1101111',
    '7': '1110010',
    '8': '1111111',
    '9': '1111011',
    ' ': '0000000',
}

T = int(input())

for i in range(T):
    A, B = input().split()
    A = (5 - len(A)) * ' ' + A
    B = (5 - len(B)) * ' ' + B
    total = 0

    for x in range(5):
        for j in range(7):
            total += (light[A[x]][j] != light[B[x]][j])
    print(total)
