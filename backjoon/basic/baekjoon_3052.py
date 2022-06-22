#Baejoon_3052
import sys

remaindList = [0 for _ in range(10)]
B = 42
for x in range(10):
    num = int(input())
    remaindList[x] = num % B
dicremaind = set(remaindList)
print(len(dicremaind))