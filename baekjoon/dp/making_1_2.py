"""
Baekjoon 12852 1로 만들기

"""

import sys

N = int(input())
dp = [sys.maxsize] * (N + 1)
dp[N] = 0

for i in range(N, 1, -1):
    if i % 3 == 0:
        dp[i // 3] = min(dp[i // 3], dp[i] + 1)
    if i % 2 == 0:
        dp[i // 2] = min(dp[i // 2], dp[i] + 1)
    dp[i - 1] = min(dp[i - 1], dp[i] + 1)

print(dp[1])

answer = [1]
i = 1
while i != N:
    current = dp[i]
    if i * 3 <= N and dp[i * 3] == current - 1:
        answer.append(i * 3)
        i = i * 3
    elif i * 2 <= N and dp[i * 2] == current - 1:
        answer.append(i * 2)
        i = i * 2
    else:
        answer.append(i + 1)
        i = i + 1

for i in range(dp[1], -1, -1):
    print(answer[i], "", end='')
