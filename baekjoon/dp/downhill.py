"""
Baekjoon 1520 내리막 길

"""

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

M, N = list(map(int, input().split()))
m = [list(map(int, input().split())) for _ in range(M)]
dp = [[0] * N for _ in range(M)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    answer = 0
    if x == N - 1 and y == M - 1:
        return 1
    elif dp[y][x] > 0:
        return dp[y][x]
    elif dp[y][x] < 0:
        return 0
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < M and m[y][x] > m[next_y][next_x]:
            answer += dfs(next_x, next_y)
    if answer == 0:
        dp[y][x] = -1
    else:
        dp[y][x] = answer
    return answer


print(dfs(0, 0))
