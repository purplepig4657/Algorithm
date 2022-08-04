"""
Baekjoon 1719 택배

"""

import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

courses = [[sys.maxsize if i != j else 0 for i in range(n)] for j in range(n)]
answer = [[i + 1 if i != j else '-' for i in range(n)] for j in range(n)]

for _ in range(m):
    u, v, w = list(map(int, input().split()))
    courses[u - 1][v - 1] = w
    courses[v - 1][u - 1] = w


def floyd_warshall(m, a):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if j == k:
                    continue
                if m[j][i] + m[i][k] < m[j][k]:
                    m[j][k] = m[j][i] + m[i][k]
                    a[j][k] = a[j][i]


floyd_warshall(courses, answer)
for ans in answer:
    print(*ans)
