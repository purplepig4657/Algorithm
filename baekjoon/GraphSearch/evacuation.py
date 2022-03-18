"""
Baekjoon 3055 탈출

"""

import sys
input = sys.stdin.readline
from collections import deque

R, C = list(map(int, input().split()))
m = []
wave_queue = deque()
hedgehog = ()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(R):
    tmp = list(input())
    for j in range(C):
        if tmp[j] == '*':
            wave_queue.append((j, i, 0))
            tmp[j] = 0
        elif tmp[j] == '.':
            tmp[j] = -1
        elif tmp[j] == 'S':
            tmp[j] = 'S'
            hedgehog = (j, i)
    m.append(tmp[:-1])


def wave_bfs(m):
    visited = [[False] * C for _ in range(R)]
    while wave_queue:
        now = wave_queue.popleft()
        visited[now[1]][now[0]] = True
        for i in range(4):
            next_x = now[0] + dx[i]
            next_y = now[1] + dy[i]
            if 0 <= next_x < C and 0 <= next_y < R and not visited[next_y][next_x] and m[next_y][next_x] != 'D' \
                    and m[next_y][next_x] != 'X':
                wave_queue.append((next_x, next_y, now[2] + 1))
                m[next_y][next_x] = now[2] + 1
                visited[next_y][next_x] = True


wave_bfs(m)


def hedgehog_bfs(x, y):
    visited = [[False] * C for _ in range(R)]
    queue = deque()
    queue.append((x, y, 1))
    while queue:
        now = queue.popleft()
        visited[now[1]][now[0]] = True
        for i in range(4):
            next_x = now[0] + dx[i]
            next_y = now[1] + dy[i]
            if 0 <= next_x < C and 0 <= next_y < R and not visited[next_y][next_x] and m[next_y][next_x] != 'X':
                if m[next_y][next_x] == 'D':
                    return now[2]
                if m[next_y][next_x] > now[2] or m[next_y][next_x] == -1:
                    queue.append((next_x, next_y, now[2] + 1))
                    visited[next_y][next_x] = True
    return "KAKTUS"


answer = hedgehog_bfs(hedgehog[0], hedgehog[1])
print(answer)
