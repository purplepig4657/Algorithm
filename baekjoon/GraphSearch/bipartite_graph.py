"""
Baekjoon 1707 이분 그래프

"""

import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def bfs(m, color, start_node):
    queue = deque()
    queue.append(start_node)
    color[start_node] = 1
    while queue:
        now = queue.popleft()
        for node in m[now]:
            if color[node] == 0:
                queue.append(node)
                color[node] = -1 * color[now]
            else:
                if color[node] == color[now]:
                    return False
    if 0 in color:
        return bfs(m, color, color.index(0))
    return True


K = int(input())
for _ in range(K):
    V, E = list(map(int, input().split()))
    m = [[] for _ in range(V + 1)]
    color = [0] * (V + 1)
    color[0] = [-1]
    for _ in range(E):
        u, v = list(map(int, input().split()))
        m[u].append(v)
        m[v].append(u)

    print("YES" if bfs(m, color, 1) else "NO")
