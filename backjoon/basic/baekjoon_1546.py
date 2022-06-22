#Baejoon 1546

count = int(input())
scoreList = list(map(int, input().split()))
maxScore = max(scoreList)

for x in range(len(scoreList)):
    scoreList[x] = (scoreList[x]/maxScore)*100
print((sum(scoreList[::]))/len(scoreList))