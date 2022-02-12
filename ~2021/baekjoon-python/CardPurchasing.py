N = int(input())
dp = list(map(int, input().split()))

for i in range(N - 1):
    for j in range(int((i + 1) / 2) + 1):
        dp[i + 1] = max(dp[i + 1], dp[i - j] + dp[j])

print(dp[N - 1])

'''
import sys

N = int(sys.stdin.readline())
dp = list(map(int, sys.stdin.readline().split()))

for i in range(N - 1):
    for j in range(int((i + 1) / 2) + 1):
        dp[i + 1] = max(dp[i + 1], dp[i - j] + dp[j])

print(dp[N - 1])
'''
