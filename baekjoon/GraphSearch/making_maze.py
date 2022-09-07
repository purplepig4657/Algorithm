"""
Baekjoon 2665 미로만들기

"""

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = [list(map(int, input()[:-1])) for _ in range(n)]
answer = [[-1] * n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(answer):
    queue = deque()
    queue.appendleft((0, 0))
    answer[0][0] = 0
    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == n - 1:
            return
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < n and answer[next_y][next_x] == -1:
                if m[next_y][next_x] == 1:
                    answer[next_y][next_x] = answer[y][x]
                    queue.appendleft((next_x, next_y))
                else:
                    answer[next_y][next_x] = answer[y][x] + 1
                    queue.append((next_x, next_y))


bfs(answer)
print(answer[n - 1][n - 1])
