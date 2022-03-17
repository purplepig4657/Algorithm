"""
Baekjoon 2573 빙산

"""

import sys
from collections import deque
input = sys.stdin.readline

N, M = list(map(int, input().split()))
m = [list(map(int, input().split())) for _ in range(N)]
iceberg_list = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    for j in range(M):
        if m[i][j] != 0:
            iceberg_list.append([j, i, m[i][j]])


def bfs(x, y, list_length):
    queue = deque()
    queue.append((x, y))
    count = 1
    visited = [[False] * M for _ in range(N)]
    visited[y][x] = True
    while queue:
        now = queue.popleft()
        for i in range(4):
            next_x = now[0] + dx[i]
            next_y = now[1] + dy[i]
            if 0 <= next_x < M and 0 <= next_y < N and not visited[next_y][next_x] and m[next_y][next_x] > 0:
                queue.append((next_x, next_y))
                count += 1
                visited[next_y][next_x] = True
    if count != list_length:
        return False
    return True


answer = 0
iceberg_list_length = len(iceberg_list)
while iceberg_list_length > 0:
    for i in range(len(iceberg_list)):
        if iceberg_list[i] != -1:
            if not bfs(iceberg_list[i][0], iceberg_list[i][1], iceberg_list_length):
                print(answer)
                exit()
            break
    answer += 1
    remove = []
    for i in range(len(iceberg_list)):
        if iceberg_list[i] != -1:
            for j in range(4):
                next_x = iceberg_list[i][0] + dx[j]
                next_y = iceberg_list[i][1] + dy[j]
                if 0 <= next_x < M and 0 <= next_y < N and m[next_y][next_x] == 0:
                    iceberg_list[i][2] -= 1
                    if iceberg_list[i][2] == 0:
                        remove.append(i)
                        iceberg_list_length -= 1
                        break
    for i in remove:
        m[iceberg_list[i][1]][iceberg_list[i][0]] = 0
        iceberg_list[i] = -1

print(0)
