"""
Baekjoon 11051 이항 계수 2

"""

N, K = list(map(int, input().split()))
divisor = 10007

dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = dp[1][0] = dp[1][1] = 1

for i in range(2, N + 1):
    dp[i][0] = 1
    for j in range(1, i + 1):
        dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % divisor

print(dp[N][K] % divisor)
