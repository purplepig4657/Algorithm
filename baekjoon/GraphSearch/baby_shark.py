"""
Baekjoon 16236 아기 상어

"""

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
start = [0, 0]

for i in range(N):
    if 9 in m[i]:
        start[1] = i
        start[0] = m[i].index(9)
        break


def bfs(x, y, size):
    queue = deque()
    queue.append((x, y, 0))
    visited = [[False] * N for _ in range(N)]
    visited[y][x] = True
    shortest_prey = (1001, 1001, 2001)
    while queue:
        now = queue.popleft()
        for i in range(4):
            next_x = now[0] + dx[i]
            next_y = now[1] + dy[i]
            if 0 <= next_x < N and 0 <= next_y < N and m[next_y][next_x] <= size and not visited[next_y][next_x]:
                queue.append((next_x, next_y, now[2] + 1))
                visited[next_y][next_x] = True
                if 0 < m[next_y][next_x] < size and now[2] + 1 <= shortest_prey[2]:
                    if next_y < shortest_prey[1]:
                        shortest_prey = (next_x, next_y, now[2] + 1)
                    elif next_y == shortest_prey[1]:
                        if next_x < shortest_prey[0]:
                            shortest_prey = (next_x, next_y, now[2] + 1)
    return shortest_prey


shark_size = 2
eat_count = 0
answer = 0
m[start[1]][start[0]] = 0
prey = bfs(start[0], start[1], shark_size)

while prey != (1001, 1001, 2001):
    answer += prey[2]
    eat_count += 1
    m[prey[1]][prey[0]] = 0
    if eat_count == shark_size:
        shark_size += 1
        eat_count = 0
    prey = bfs(prey[0], prey[1], shark_size)

print(answer)
