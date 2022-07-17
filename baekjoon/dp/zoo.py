"""
Baekjoon 1309 동물원

"""

N = int(input())

dp = [0] * 100001

dp[0] = 1
dp[1] = 2
dp[2] = 4

for i in range(3, N + 1):
    dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 9901

print(sum(dp[:N + 1]) % 9901)
