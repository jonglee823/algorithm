#Baekjoon_ 8958
# OX quiz

line = int(input())
for _ in range(line):
    strList = input()
    sco = 0
    totalScore = 0
    for x in range(len(strList)):
        if(strList[x] == "O"):
            sco+=1
        else:
            sco=0
        totalScore += sco
    print(totalScore)