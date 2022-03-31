"""
Baekjoon 1448 삼각형 만들기

"""

import sys
input = sys.stdin.readline

N = int(input())
straw = [int(input()) for _ in range(N)]
straw.sort(reverse=True)

for i in range(2, N):
    if straw[i - 2] < straw[i - 1] + straw[i]:
        print(straw[i] + straw[i - 1] + straw[i - 2])
        exit()

print(-1)
