"""
Baekjoon 11060 점프 점프

"""

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dp = [sys.maxsize] * N
dp[0] = 0

for i in range(N):
    for j in range(i + 1, i + A[i] + 1):
        if j < N:
            dp[j] = min(dp[i] + 1, dp[j])

print(dp[N - 1] if dp[N - 1] is not sys.maxsize else -1)
