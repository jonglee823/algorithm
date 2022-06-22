#baekjoon_2798
#블랙잭

import sys

N, M = map(int, input().split())
card = list(map(int, input().strip().split()))
sum = 0

for i in range(0, N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if (card[i] + card[j] + card[k]) == M:
                sum = M
                break
            if (card[i] + card[j] + card[k]) < M and M - (card[i] + card[j] + card[k]) < M - sum:
                sum = card[i] + card[j] + card[k]
print(sum)