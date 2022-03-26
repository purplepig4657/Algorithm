"""
Baekjoon 13164 행복 유치원

"""

import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))
kids = list(map(int, input().split()))

kids.sort()
diff = []

for i in range(1, N):
    diff.append(kids[i] - kids[i - 1])

diff.sort(reverse=True)
print(sum(diff[K - 1:]))
