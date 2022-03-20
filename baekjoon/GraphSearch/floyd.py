"""
Baekjoon 11404 플로이드

"""

import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
maximum = sys.maxsize

m = [[maximum] * N for _ in range(N)]

for _ in range(M):
    u, v, w = list(map(int, input().split()))
    m[u - 1][v - 1] = min(m[u - 1][v - 1], w)

for i in range(N):
    m[i][i] = 0


def floyd_warshall(m):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                m[j][k] = min(m[j][k], m[j][i] + m[i][k])


floyd_warshall(m)
for i in range(N):
    for j in range(N):
        if m[i][j] == maximum:
            print(0, end=' ')
        else:
            print(m[i][j], end=' ')
    print()
