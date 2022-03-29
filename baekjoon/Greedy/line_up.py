"""
Baekjoon 7570 줄 세우기

"""

N = int(input())
nums = list(map(int, input().split()))
dp = [0] * 10000001

for i in nums:
    dp[i] = dp[i - 1] + 1

print(N - max(dp))
