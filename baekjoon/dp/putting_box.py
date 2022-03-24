"""
Baekjoon 1965 상자넣기

"""

n = int(input())
box = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i, -1, -1):
        if box[i] > box[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
