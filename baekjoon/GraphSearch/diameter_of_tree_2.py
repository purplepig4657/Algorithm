"""
Baekjoon 1167 트리의 지름

"""

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

V = int(input())
m = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)

for _ in range(V):
    arr = list(map(int, input().split()))
    node = arr[0]
    for i in range(1, len(arr) - 1, 2):
        m[node].append((arr[i], arr[i + 1]))


def dfs(n):
    visited[n[0]] = True
    max_dist = 0
    ans = [0]
    tmp = []
    for i in m[n[0]]:
        if not visited[i[0]]:
            md, a = dfs(i)
            md += i[1]
            if len(tmp) < 2:
                tmp.append(md)
            else:
                if min(tmp) < md:
                    tmp[tmp.index(min(tmp))] = md
            max_dist = max(max_dist, md)
            ans.append(a)
    ans[0] = sum(tmp)
    return max_dist, max(ans)


print(dfs((1, 0))[1])
