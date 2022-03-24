"""
Baekjoon 2294 동전 2

"""

import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))
dp = [sys.maxsize] * (k + 1)
coins = []
dp[0] = 0

for _ in range(n):
    value = int(input())
    if value <= k:
        coins.append(value)

coins = list(set(coins))
sorted(coins)

for i in range(len(coins)):
    for j in range(coins[i], k + 1):
        dp[j] = min(dp[j], dp[j - coins[i]] + 1)

if dp[k] == sys.maxsize:
    print(-1)
else:
    print(dp[k])
