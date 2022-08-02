"""
Baekjoon 16954 움직이는 미로 탈출

"""

import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1, 1, 1, -1, -1, 0]
dy = [1, -1, 0, 0, 1, -1, 1, -1, 0]
m = [list(input()) for _ in range(8)]
queue = deque()


def move(m):
    for i in range(8):
        for j in range(8):
            if m[i][j] == '#':
                queue.append((i, j))

    changed = []
    while queue:
        y, x = queue.popleft()
        if not (y, x) in changed:
            m[y][x] = '.'
        if 0 <= y + 1 < 8:
            m[y + 1][x] = '#'
            changed.append((y + 1, x))


def bfs(x, y, m):
    queue = deque()
    queue.append((x, y))
    count = 1
    time = 0
    while queue:
        if count == 0:
            count = time
            time = 0
            move(m)
        now_x, now_y = queue.popleft()
        if m[now_y][now_x] == '#':
            count -= 1
            continue
        for i in range(9):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]
            if 0 <= next_x < 8 and 0 <= next_y < 8 and m[next_y][next_x] == '.':
                if next_x == 7 and next_y == 0:
                    return True
                queue.append((next_x, next_y))
                time += 1
        count -= 1

    return False


print(1 if bfs(0, 7, m) else 0)
