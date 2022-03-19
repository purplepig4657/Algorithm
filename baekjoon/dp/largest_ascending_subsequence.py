"""
Baekjoon 11055 가장 큰 증가 부분 수열

"""

import sys
input = sys.stdin.readline
N = int(input())
A = [0]
A.extend(list(map(int, input().split())))

answer = 0
dp = [0] * (N + 1)

for i in range(1, N + 1):
    answer = max(answer, dp[i - 1])
    maximum = 0
    for j in range(i, -1, -1):
        if A[j] < A[i]:
            maximum = max(maximum, dp[j])
    dp[i] = maximum + A[i]

answer = max(answer, dp[N])
print(answer)
