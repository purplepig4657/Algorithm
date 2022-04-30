"""
Baekjoon 10026 적록색약

"""

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
m = [input() for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited1 = [[False] * N for _ in range(N)]
visited2 = [[False] * N for _ in range(N)]


def dfs(x, y, has_weakness, visited):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True
    color = m[y][x]
    while queue:
        now = queue.popleft()
        x = now[0]
        y = now[1]
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < N:
                p = False
                if has_weakness and not color == 'B' and not m[next_y][next_x] == 'B':
                    p = True
                if not visited[next_y][next_x] and (m[next_y][next_x] == color or p):
                    visited[next_y][next_x] = True
                    queue.append((next_x, next_y))


answer = [0, 0]
for y in range(N):
    for x in range(N):
        if not visited1[y][x]:
            answer[0] += 1
            dfs(x, y, False, visited1)
        if not visited2[y][x]:
            answer[1] += 1
            dfs(x, y, True, visited2)

print(answer[0], answer[1])
