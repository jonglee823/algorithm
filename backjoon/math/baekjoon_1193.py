#baekjoon_1193
#분수찾기
from fractions import Fraction
# 분모 denominator
# 분자 molecule

inputNum = int(input())
totalCount = 0
index=0

while totalCount < inputNum:
    index += 1
    totalCount += index

gap = totalCount - inputNum
if index % 2 == 0:
    molecule = index - gap
    denominator = gap + 1
else:
    molecule = gap + 1
    denominator = index - gap
print(f'{molecule}/{denominator}')

