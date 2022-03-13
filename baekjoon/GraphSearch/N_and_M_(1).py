"""
Baekjoon 15649 N과 M (1)

"""
import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))

visited = [False] * (N + 1)
seq = [0] * (M + 1)


def dfs(depth, seq):
    if depth == M:
        for i in seq[1:]:
            print(f"{i} ", end='')
        print()
        return
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            seq[depth + 1] = i
            dfs(depth + 1, seq)
            visited[i] = False


for i in range(1, N + 1):
    visited[i] = True
    seq[1] = i
    dfs(1, seq)
    visited[i] = False
