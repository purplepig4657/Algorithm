"""
Baekjoon 1937 욕심쟁이 판다

"""

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
dp = [[1] * n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, dp):
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < n and 0 <= next_y < n and forest[y][x] < forest[next_y][next_x]:
            if dp[next_y][next_x] == 1:
                dp[y][x] = max(dp[y][x], dfs(next_x, next_y, dp) + 1)
            else:
                dp[y][x] = max(dp[y][x], dp[next_y][next_x] + 1)

    return dp[y][x]


answer = 0
for y in range(n):
    for x in range(n):
        if dp[y][x] == 1:
            answer = max(answer, dfs(x, y, dp))

print(answer)

# print(max(max(dp)))
# 이렇게 한다면 2차원 배열의 최대값을 구할 수 있는 줄 알아서 계속 틀렸다.
# 2차원 배열에 max 함수를 쓴다면, 2차원 배열의 1차원 배열들 중, 첫 번째 원소가 가장 큰 배열을 반환하게 된다. 때문에 틀린 코드다.
