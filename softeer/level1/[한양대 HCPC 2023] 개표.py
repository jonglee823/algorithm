import sys

t = int(input())

result = []

for i in range(t):
    result.append(int(input()))

for num in result:

    temp = ''
    i = (num // 5)
    while i >= 1:
        if i == 1 and num % 5 == 0:
            temp += '++++'
            break
        temp += '++++ '
        i -= 1

    temp = temp + (num % 5) * '|'

    print(temp)