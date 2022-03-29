"""
Baekjoon 2109 순회강연

"""

import sys
input = sys.stdin.readline

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]

info.sort(key=lambda x: (-x[0], x[1]))

visited = [0] * 10001

for i in range(n):
    for j in range(info[i][1], 0, -1):
        if visited[j] == 0:
            visited[j] = info[i][0]
            break

print(sum(visited))
