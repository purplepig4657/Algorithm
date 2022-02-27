"""
Baekjoon 1976 여행 가자

"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    M = int(input())
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


    for i in range(1, N + 1):
        c = list(map(int, input().split()))
        for j in range(N):
            if c[j] == 1:
                union(i, j + 1)

    c = list(map(int, input().split()))
    p = find(c[0])

    for i in range(1, M):
        tmp = find(c[i])
        if p != tmp:
            print("NO")
            exit()

    print("YES")
