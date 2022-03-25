"""
Baekjoon 2589 보물섬

"""

import sys
from collections import deque
input = sys.stdin.readline

N, M = list(map(int, input().split()))
m = [list(input()) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y, 0))
    max_dist = 0
    visited = [[False] * M for _ in range(N)]
    visited[y][x] = True
    while queue:
        now = queue.popleft()
        x = now[0]
        y = now[1]
        dist = now[2]
        max_dist = max(max_dist, dist)
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < M and 0 <= next_y < N and not visited[next_y][next_x] \
                    and m[next_y][next_x] == 'L':
                queue.append((next_x, next_y, dist + 1))
                visited[next_y][next_x] = True
    return max_dist


answer = 0
for i in range(N):
    for j in range(M):
        if m[i][j] == 'L':
            answer = max(answer, bfs(j, i))

print(answer)
