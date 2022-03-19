"""
Baekjoon 1890 점프

"""

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dx = [1, 0]
dy = [0, 1]


def dfs(x, y):
    answer = 0
    if x == N - 1 and y == N - 1:
        return 1
    elif m[y][x] == 0:
        return 0
    for i in range(2):
        next_x = x + dx[i] * m[y][x]
        next_y = y + dy[i] * m[y][x]
        if 0 <= next_x < N and 0 <= next_y < N:
            if dp[next_y][next_x] > 0:
                answer += dp[next_y][next_x]
            else:
                answer += dfs(next_x, next_y)
    dp[y][x] = answer
    return answer


print(dfs(0, 0))
