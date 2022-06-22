#BAEKJOON 5622

dialAlpha = {"A":2,"B":2,"C":2,"D":3,"E":3,"F":3,"G":4,"H":4,"I":4,"J":5,"K":5,"L":5,"M":6,"N":6,"O":6,"P":7,"Q":7,"R":7,"S":7,"T":8,"U":8,"V":8,"W":9,"X":9,"Y":9,"Z":9}
dialNumber=[x for x in range(1, 11)]

inputString = list(str(input()))
time = 0
for index in range(len(inputString)):
    time = time + dialAlpha.get(inputString[index]) +1
print(time)