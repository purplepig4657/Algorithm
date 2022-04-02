"""
Baekjoon 16234 인구 이동

"""

import sys
from collections import deque
input = sys.stdin.readline

N, L, R = list(map(int, input().split()))
m = [list(map(int, input().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, m, visited):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True
    open = [(x, y)]
    sum_all = m[y][x]
    while queue:
        now = queue.popleft()
        x, y = now[0], now[1]
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < N and \
                    not visited[next_y][next_x] and L <= abs(m[y][x] - m[next_y][next_x]) <= R:
                open.append((next_x, next_y))
                visited[next_y][next_x] = True
                queue.append((next_x, next_y))
                sum_all += m[next_y][next_x]
    return open, sum_all


answer = 0
while True:
    visited = [[False] * N for _ in range(N)]
    is_end = True
    for i in range(N):
        for j in range(N):
            if not visited[j][i]:
                open, sum_all = bfs(i, j, m, visited)
                sum_all = int(sum_all / len(open))
                if len(open) > 1:
                    is_end = False
                    for p in open:
                        m[p[1]][p[0]] = sum_all
    if is_end:
        break
    answer += 1

print(answer)
