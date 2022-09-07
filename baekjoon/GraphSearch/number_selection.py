"""
Baekjoon 2668 숫자고르기

"""

import sys
input = sys.stdin.readline

N = int(input())
m = [0]
for _ in range(N):
    m.append(int(input()))


def dfs(n):
    visited = [False] * (N + 1)
    visited_node = []
    node = n
    while not visited[node]:
        visited_node.append(node)
        visited[node] = True
        node = m[node]

    return visited_node if node == n else None


answer = []
for i in range(1, N + 1):
    if i not in answer:
        result = dfs(i)
        if result:
            answer.extend(result)

answer.sort()
print(len(answer))
for node in answer:
    print(node)
