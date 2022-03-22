"""
Baekjoon 2206 벽 부수고 이동하기

"""

import sys
from collections import deque
input = sys.stdin.readline

N, M = list(map(int, input().split()))
m = [list(map(int, input()[:-1])) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    visited1 = [[False] * M for _ in range(N)]
    visited2 = [[False] * M for _ in range(N)]
    queue = deque()
    queue.append((0, 0, False, 1))
    answer = sys.maxsize
    while queue:
        node = queue.popleft()
        x = node[0]
        y = node[1]
        was_break = node[2]
        depth = node[3]
        if x == M - 1 and y == N - 1:
            answer = min(answer, depth)
            continue
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < M and 0 <= next_y < N:
                if m[next_y][next_x] == 1 and not was_break and not visited2[next_y][next_x]:
                    queue.append((next_x, next_y, True, depth + 1))
                    visited2[next_y][next_x] = True
                elif m[next_y][next_x] == 0 and not was_break and not visited1[next_y][next_x]:
                    queue.append((next_x, next_y, was_break, depth + 1))
                    visited1[next_y][next_x] = True
                elif m[next_y][next_x] == 0 and was_break and not visited2[next_y][next_x]:
                    queue.append((next_x, next_y, was_break, depth + 1))
                    visited2[next_y][next_x] = True
    if answer == sys.maxsize:
        return -1
    return answer


print(bfs())
