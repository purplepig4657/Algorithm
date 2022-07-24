"""
Baekjoon 6593 빌딩

"""

import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dl = [0, 0, 0, 0, 1, -1]


def bfs(p, m, visited):
    queue = deque()
    queue.append(p)
    visited[p[0]][p[2]][p[1]] = True
    while queue:
        now = queue.popleft()
        for i in range(6):
            next_l = now[0] + dl[i]
            next_x = now[1] + dx[i]
            next_y = now[2] + dy[i]
            if 0 <= next_l < L and 0 <= next_x < C and 0 <= next_y < R and not visited[next_l][next_y][next_x]:
                if m[next_l][next_y][next_x] == '.':
                    queue.append((next_l, next_x, next_y, now[3] + 1))
                    visited[next_l][next_y][next_x] = True
                elif m[next_l][next_y][next_x] == 'E':
                    return now[3] + 1
    return -1


while True:
    L, R, C = list(map(int, input().split()))
    if L == 0 and R == 0 and C == 0:
        break
    m = list()
    for _ in range(L):
        m.append([list(input()) for _ in range(R)])
        input()

    p = tuple()
    for l in range(L):
        for y in range(R):
            for x in range(C):
                if m[l][y][x] == 'S':
                    p = (l, x, y, 0)
                    break

    visited = [[[False] * C for _ in range(R)] for _ in range(L)]
    answer = bfs(p, m, visited)
    print(f"Escaped in {answer} minute(s)." if answer > 0 else "Trapped!")
