"""
Baekjoon 14442 벽 부수고 이동하기 2

"""

import sys
from collections import deque
input = sys.stdin.readline

N, M, K = list(map(int, input().split()))
m = [list(map(int, input()[:-1])) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[[sys.maxsize] * M for _ in range(N)] for _ in range(K + 1)]


def bfs(visited):
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0][0] = 1
    while queue:
        x, y, break_count = queue.popleft()
        for i in range(4):
            next_x, next_y = x + dx[i], y + dy[i]
            if 0 <= next_x < M and 0 <= next_y < N:
                if m[next_y][next_x] == 0 and visited[break_count][next_y][next_x] > visited[break_count][y][x] + 1:
                    visited[break_count][next_y][next_x] = visited[break_count][y][x] + 1
                    queue.append((next_x, next_y, break_count))
                elif m[next_y][next_x] == 1 and break_count + 1 <= K \
                        and visited[break_count + 1][next_y][next_x] > visited[break_count][y][x] + 1:
                    visited[break_count + 1][next_y][next_x] = visited[break_count][y][x] + 1
                    queue.append((next_x, next_y, break_count + 1))


bfs(visited)
answer = sys.maxsize
for i in range(K + 1):
    answer = min(answer, visited[i][N - 1][M - 1])
print(answer if answer is not sys.maxsize else -1)
