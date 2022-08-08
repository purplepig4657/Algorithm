"""
Baekjoon 12970 AB

"""

import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))
nums = []

for i in range(N, -1, -1):
    if i * (N - i) >= K:
        nums = [0] * (i + 1)
        for _ in range(N):
            if K >= i:
                nums[i] += 1
                K -= i
            else:
                nums[K] += 1
                K -= K
        break

answer = ''
if not nums:
    print(-1)
else:
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] > 0:
            answer += 'A' * nums[i] + 'B'
        else:
            answer += 'B'

print(answer)
