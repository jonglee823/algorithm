#dice 3
from collections import Counter

diceList= list(map(int, input().split()))
reward = 0

deDupliList=set(diceList)

if(len(deDupliList) == 1 ):
    reward = 10000 +(diceList[0] * 1000)
elif(len(deDupliList) == 2):
    result = Counter(diceList)
    for key,value in result.items():
        if value >= 2:
            reward = 1000 + (key * 100)
else:
    reward += max(diceList)*100

print(reward)
