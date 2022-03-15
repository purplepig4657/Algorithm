"""
Baekjoon 1967 트리의 지름

"""

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
m = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(n - 1):
    u, v, w = list(map(int, input().split()))
    m[u].append((v, w))


def dfs(n):
    max_dist = 0
    ans = [0]
    tmp = []
    for i in m[n[0]]:
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
