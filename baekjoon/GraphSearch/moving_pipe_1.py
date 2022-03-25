"""
Baekjoon 17070 파이프 옮기기 1

"""

import sys
input = sys.stdin.readline

N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]
dx = [0, 1, 1]
dy = [1, 0, 1]

if m[N - 1][N - 1] == 1:
    print(0)
    exit()


def dfs(x, y, status):
    answer = 0
    if x == N - 1 and y == N - 1:
        return 1
    for i in range(3):
        if i != 2 and i == status:
            continue
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < N and 0 <= next_y < N and m[next_y][next_x] == 0:
            if i == 2 and m[y + 1][x] == 0 and m[y][x + 1] == 0:
                answer += dfs(next_x, next_y, i)
                continue
            elif i != 2:
                answer += dfs(next_x, next_y, abs(i - 1))

    return answer


print(dfs(1, 0, 0))
