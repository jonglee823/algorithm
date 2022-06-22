# #baekjoon 4344
import sys
row = int(input())
scoreList = []
for i in range(row):
    scoreList.append(list(map(int, sys.stdin.readline().split())))
count = [0 for _ in range(row)]
for x in range(len(scoreList)):
    average = 0
    for y in range(len(scoreList[x])):
        if(y==0):
            continue
        else:
            average +=scoreList[x][y]
    count[x] = int(average/scoreList[x][0])
for x in range(len(scoreList)):
    realCount = 0
    for y in range(len(scoreList[x])):
        if(y==0):
            continue
        else:
            if(count[x] < scoreList[x][y]):
                realCount+=1
    print('%.3f%%' % ( realCount/(scoreList[x][0]) * 100.0))


#인터넷에서 찾은거.. 색다른 관점이다.. 입력 받으면서 로직 돌려도됨...
# 출처 : https://www.acmicpc.net/problem/4344
# num = int(input())
# for i in range(num):
#     sco = list(map(int, input().split()))
#     avg = sum(sco[1:])/sco[0]
#     cnt = 0
#     for j in sco[1:]:
#         if j > avg:
#             cnt+=1
#     print("%.3f%%"%round(cnt/sco[0]*100,3))