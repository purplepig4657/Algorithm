"""
Baekjoon 11725 트리의 부모 찾기

"""

'''
# 인접 행렬 DFS
N = int(input())
m = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = list(map(int, input().split()))
    m[a][b] = m[b][a] = 1

answer = [0] * (N + 1)
answer[1] = 1


def dfs(n, parent):
    answer[n] = parent
    for i in range(1, N + 1):
        if m[n][i] == 1 and answer[i] == 0:
            dfs(i, n)


dfs(1, 1)

for i in answer[2:]:
    print(i)
'''

'''
# 인접 리스트 DFS
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N = int(input())
m = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = list(map(int, input().split()))
    m[a].append(b)
    m[b].append(a)

answer = [0] * (N + 1)
answer[1] = 1


def dfs(n, parent):
    answer[n] = parent
    for i in m[n]:
        if answer[i] == 0:
            dfs(i, n)


dfs(1, 1)

for i in answer[2:]:
    print(i)
'''

# 인접 리스트 DFS 반복문
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
m = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = list(map(int, input().split()))
    m[a].append(b)
    m[b].append(a)

answer = [0] * (N + 1)
answer[1] = 1
queue = deque()
queue.appendleft(1)


def dfs():
    while queue:
        node = queue.popleft()

        for i in m[node]:
            if answer[i] == 0:
                answer[i] = node
                queue.appendleft(i)


dfs()

for i in answer[2:]:
    print(i)
