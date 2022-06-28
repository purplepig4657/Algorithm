"""
Baekjoon 1325 효율적인 해킹

"""

import sys
from collections import deque

input = sys.stdin.readline

N, M = list(map(int, input().split()))

m = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = list(map(int, input().split()))
    m[B].append(A)

max_value = 0
answer = []

for i in range(1, N + 1):
    visit = [False] * (N + 1)
    current_value = 0
    queue = deque()
    queue.append(i)
    visit[i] = True
    while queue:
        now = queue.popleft()
        for j in range(len(m[now])):
            if not visit[m[now][j]]:
                queue.append(m[now][j])
                visit[m[now][j]] = True
        current_value += 1
    if current_value > max_value:
        max_value = current_value
        answer.clear()
        answer.append(i)
    elif current_value == max_value:
        answer.append(i)

for i in range(len(answer)):
    print(answer[i], end=' ')
