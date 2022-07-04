"""
Baekjoon 1956 운동

"""

import sys
input = sys.stdin.readline

V, E = list(map(int, input().split()))

m = [[sys.maxsize] * V for _ in range(V)]

for _ in range(E):
    a, b, c = list(map(int, input().split()))
    if m[a - 1][b - 1] > c:
        m[a - 1][b - 1] = c


def floyd_warshall(m):
    for i in range(V):
        for j in range(V):
            for k in range(V):
                m[j][k] = min(m[j][k], m[j][i] + m[i][k])


floyd_warshall(m)

answer = sys.maxsize
for i in range(V):
    answer = min(answer, m[i][i])

print(answer if answer != sys.maxsize else -1)
