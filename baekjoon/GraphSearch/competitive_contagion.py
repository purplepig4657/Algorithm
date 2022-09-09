"""
Baekjoon 18405 경쟁적 전염

"""

import sys
from collections import deque
input = sys.stdin.readline

N, K = list(map(int, input().split()))
m = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = list(map(int, input().split()))
virus = [[] for _ in range(K + 1)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
queue = deque()

for y in range(N):
    for x in range(N):
        if m[y][x] != 0:
            virus[m[y][x]].append((x, y, m[y][x], 0))


def bfs():
    visited = [[False] * N for _ in range(N)]
    for v in virus:
        if len(v) != 0:
            for cor in v:
                visited[cor[1]][cor[0]] = True
                queue.append(cor)
    while queue:
        x, y, n, depth = queue.popleft()
        if depth >= S:
            continue
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < N and not visited[next_y][next_x]:
                visited[next_y][next_x] = True
                m[next_y][next_x] = n
                queue.append((next_x, next_y, n, depth + 1))


bfs()
print(m[X - 1][Y - 1])
