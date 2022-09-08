"""
Baekjoon 2252 줄 세우기

"""

import sys
from collections import deque
input = sys.stdin.readline

N, M = list(map(int, input().split()))
m = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
answer = deque()

for _ in range(M):
    u, v = list(map(int, input().split()))
    m[v].append(u)
    in_degree[u] += 1

queue = deque()
for i in range(1, N + 1):
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    node = queue.popleft()
    answer.appendleft(node)
    for n in m[node]:
        if in_degree[n] == 0:
            continue
        in_degree[n] -= 1
        if in_degree[n] == 0:
            queue.append(n)

while answer:
    print(answer.popleft(), end=' ')
