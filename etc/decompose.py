n,k = map(int, input().split())

dp = [[0] * (n+1) for _ in range(k+1)]

dp[1] = [1 for _ in range(n+1)]

for y in range(2, k+1):
    for x in range(1, n + 1):
        dp[x][y] = dp[n-x][] +


