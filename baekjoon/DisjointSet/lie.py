"""
Baekjoon 1043 거짓말

"""

import sys
input = sys.stdin.readline
N, M = list(map(int, input().split()))

parents = [i for i in range(N + 1)]
is_know = [False for _ in range(N + 1)]

for i in list(map(int, input().split()))[1:]:
    is_know[i] = True

party = [list(map(int, input().split()))[1:] for _ in range(M)]


def find(u):
    if parents[u] == u:
        return u
    parents[u] = find(parents[u])
    return parents[u]


def union(u, v):
    u = find(u)
    v = find(v)

    if is_know[u] or is_know[v]:
        if u == v:
            pass
        elif is_know[u]:
            parents[v] = u
        else:
            parents[u] = v
        return True
    else:
        if u == v:
            pass
        elif u < v:
            parents[v] = u
        else:
            parents[u] = v
        return False


answer = 0
for i in range(M):
    for j in range(1, len(party[i])):
        union(party[i][j], party[i][j - 1])

for i in range(M):
    answer += 1
    for j in party[i]:
        if is_know[find(j)]:
            answer -= 1
            break


print(answer)
