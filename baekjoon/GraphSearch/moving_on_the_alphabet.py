"""
Baekjoon 1987 알파벳

"""

''' 틀림
import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

R, C = list(map(int, input().split()))

m = [[] for _ in range(R + 2)]
m[0] = m[R + 1] = [0] * (C + 2)

for i in range(1, R + 1):
    alphabets = input()
    for alphabet in alphabets:
        if alphabet != '\n':
            m[i].append(ord(alphabet))
    m[i].insert(0, 0)
    m[i].append(0)

queue = deque()
queue.appendleft((1, 1, [m[1][1]], 1))
move_ref = [(-1, 0), (0, 1), (1, 0), (0, -1)]
answer = 0

while queue:
    now_x, now_y, visited, dist = queue.popleft()
    canMove = False
    for ref in move_ref:
        x = now_x + ref[0]
        y = now_y + ref[1]
        if m[x][y] != 0 and m[x][y] not in visited:
            canMove = True
            visited_tmp = deepcopy(visited)
            visited_tmp.append(m[x][y])
            queue.appendleft((x, y, visited_tmp, dist + 1))
    if not canMove:
        answer = max(answer, dist)


print(answer)
'''

#  https://imksh.com/46  pypy3 메모리 초과
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

R, C = list(map(int, input().split()))
m = [list(input()) for _ in range(R)]

visited = [False] * 26
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0


def dfs(now_x, now_y, cnt):
    global answer
    answer = max(answer, cnt)
    for i in range(4):
        x, y = now_x + dx[i], now_y + dy[i]
        if 0 <= x < R and 0 <= y < C:
            now = ord(m[x][y]) - 65
            if not visited[now]:
                visited[now] = True
                dfs(x, y, cnt + 1)
                visited[now] = False


visited[ord(m[0][0]) - 65] = True
dfs(0, 0, 1)
print(answer)
