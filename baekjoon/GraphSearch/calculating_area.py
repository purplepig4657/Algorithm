"""
Baekjoon 2583 영역 구하기

"""

import sys
from collections import deque
input = sys.stdin.readline

M, N, K = list(map(int, input().split()))
m = [[0] * N for _ in range(M)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(K):
    tmp = list(map(int, input().split()))
    a = (tmp[0], tmp[1])
    b = (tmp[2], tmp[3])
    for i in range(a[0], b[0]):
        for j in range(a[1], b[1]):
            m[j][i] = 1


def bfs(p, m, visited):
    queue = deque()
    queue.append(p)
    visited[p[1]][p[0]] = True
    area = 1
    while queue:
        now = queue.popleft()
        x = now[0]
        y = now[1]
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < M and not visited[next_y][next_x] and m[next_y][next_x] == 0:
                area += 1
                queue.append((next_x, next_y))
                visited[next_y][next_x] = True

    return area


visited = [[False] * N for _ in range(M)]
area_count = 0
areas = []
for x in range(0, N):
    for y in range(0, M):
        if m[y][x] == 0 and not visited[y][x]:
            area_count += 1
            areas.append(bfs((x, y), m, visited))

areas.sort()
print(area_count)
print(*areas)
