"""
Baekjoon 10159 저울

"""

import sys
from collections import deque
input = sys.stdin.readline

N, M = int(input()), int(input())
original_direction = [[] for _ in range(N + 1)]
reversed_direction = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = list(map(int, input().split()))
    original_direction[u].append(v)
    reversed_direction[v].append(u)


def bfs(init_node):
    result = [init_node]
    visited = [False] * (N + 1)
    queue = deque()
    queue.append(init_node)
    while queue:
        node = queue.popleft()
        for n in original_direction[node]:
            if not visited[n]:
                result.append(n)
                queue.append(n)
                visited[n] = True

    visited = [False] * (N + 1)
    queue = deque()
    queue.append(init_node)
    while queue:
        node = queue.popleft()
        for n in reversed_direction[node]:
            if not visited[n]:
                result.append(n)
                queue.append(n)
                visited[n] = True

    return len(set(result))


for i in range(1, N + 1):
    print(N - bfs(i))
