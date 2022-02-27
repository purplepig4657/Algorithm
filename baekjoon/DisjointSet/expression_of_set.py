"""
Baekjoon 1717 집합의 표현

"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = list(map(int, input().split()))

    parents = [0] * (n + 1)
    for i in range(n + 1):
        parents[i] = i


    def find(u):
        if parents[u] == u:
            return u
        parents[u] = find(parents[u])
        return parents[u]


    def union(u, v):
        u = find(u)
        v = find(v)

        if u <= v:
            parents[v] = u
        else:
            parents[u] = v


    for _ in range(m):
        c = list(map(int, input().split()))

        if c[0] == 0:
            union(c[1], c[2])
        else:
            if find(c[1]) == find(c[2]):
                print("YES")
            else:
                print("NO")
