#baekjoon 10811
#바구니 뒤집기

n, m = map(int, input().split())
num = [1 + i for i in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    num[x-1:y] = reversed(num[x-1:y])
print(*num, end=' ')