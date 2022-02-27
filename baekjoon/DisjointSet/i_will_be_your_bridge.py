"""
Baekjoon 17352 여러분의 다리가 되어 드리겠습니다!

"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    parents = [0] * (N + 1)
    for i in range(N + 1):
        parents[i] = i


    def find(u):
        if parents[u] == u:
            return u
        parents[u] = find(parents[u])
        return parents[u]


    def union(u, v):
        u = find(u)
        v = find(v)

        if u == v:
            return
        if u < v:
            parents[v] = u
        else:
            parents[u] = v


    for i in range(N - 2):
        a, b = list(map(int, input().split()))
        union(a, b)

    p = find(1)
    for i in range(2, N + 1):
        tmp = find(i)
        if p != tmp:
            print(1, i)
            break
