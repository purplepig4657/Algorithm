"""
Baekjoon 2638 치즈

"""

import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

N, M = list(map(int, input().split()))
m = [list(map(int, input().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(m):
    visited = [[False] * M for _ in range(N)]
    queue = deque()
    queue.append((0, 0))
    m_copy = deepcopy(m)
    remove = []
    while queue:
        now = queue.popleft()
        x = now[0]
        y = now[1]
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < M and 0 <= next_y < N:
                if m_copy[next_y][next_x] > 0:
                    m_copy[next_y][next_x] += 1
                    if m_copy[next_y][next_x] == 3:
                        remove.append((next_x, next_y))
                if m_copy[next_y][next_x] == 0 and not visited[next_y][next_x]:
                    queue.append((next_x, next_y))
                    visited[next_y][next_x] = True
    if len(remove) > 0:
        return False, remove
    else:
        return True, remove


answer = 0
while True:
    all_melted, remove = bfs(m)
    if all_melted:
        break
    for x, y in remove:
        m[y][x] = 0
    answer += 1
print(answer)
