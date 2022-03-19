"""
Baekjoon 9663 N-Queen

"""

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
m = [[False] * N for _ in range(N)]
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]


def set_queen_map(x, y):
    history = []
    for i in range(8):
        c = 0
        while True:
            c += 1
            next_x = x + dx[i] * c
            next_y = y + dy[i] * c
            if 0 <= next_x < N and 0 <= next_y < N:
                if not m[next_y][next_x]:
                    m[next_y][next_x] = True
                    history.append((next_x, next_y))
            else:
                break
    return history


def bf(depth, m):
    answer = 0
    if depth == N:
        return 1
    for i in range(N):
        if not m[depth][i]:
            history = set_queen_map(i, depth)
            m[depth][i] = True
            answer += bf(depth + 1, m)
            m[depth][i] = False
            for location in history:
                m[location[1]][location[0]] = False
    return answer


print(bf(0, m))
