"""
Baekjoon 16929 Two Dots

"""

import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
m = [list(input()) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, initial, count, m, visited):
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if next_x == initial[0] and initial[1] == y:
            if count >= 4:
                return True
            else:
                continue
        if 0 <= next_x < M and 0 <= next_y < N and m[next_y][next_x] == initial[2] and not visited[next_y][next_x]:
            visited[next_y][next_x] = True
            if dfs(next_x, next_y, initial, count + 1, m, visited):
                return True
            visited[next_y][next_x] = False
    return False


for y in range(N):
    for x in range(M):
        visited = [[False] * M for _ in range(N)]
        if dfs(x, y, (x, y, m[y][x]), 1, m, visited):
            print("Yes")
            exit()

print("No")
