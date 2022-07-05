"""
Baekjoon 4179 불!

"""

import sys
from collections import deque
input = sys.stdin.readline

R, C = list(map(int, input().split()))
m = [list(input()[:-1]) for _ in range(R)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

J = (0, 0)
fire_queue = deque()

for i in range(R):
    for j in range(C):
        if m[i][j] == '#':
            m[i][j] = 0
        elif m[i][j] == '.':
            m[i][j] = -1
        elif m[i][j] == 'J':
            J = (j, i)
            m[i][j] = -1
        elif m[i][j] == 'F':
            fire_queue.append((j, i, 0))
            m[i][j] = 0


def bfs(x, y, m, mode):
    visited = [[False] * C for _ in range(R)]
    queue = deque()
    if mode == 0:
        while fire_queue:
            fire = fire_queue.popleft()
            queue.append((fire[0], fire[1], 0))
            visited[fire[1]][fire[0]] = True
    else:
        queue.append((x, y, 1))
        visited[y][x] = True
    while queue:
        now = queue.popleft()
        x = now[0]
        y = now[1]
        count = now[2]
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < C and 0 <= next_y < R:
                if (m[next_y][next_x] > count or m[next_y][next_x] == -1) and not visited[next_y][next_x]:
                    if mode == 0:
                        m[next_y][next_x] = count + 1
                    queue.append((next_x, next_y, count + 1))
                    visited[next_y][next_x] = True
            else:
                if mode == 0:
                    continue
                else:
                    return count
    return 'IMPOSSIBLE'


bfs(-1, -1, m, 0)
print(bfs(J[0], J[1], m, 1))
