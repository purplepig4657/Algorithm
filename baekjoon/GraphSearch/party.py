"""
Baekjoon 1238 파티

"""

'''
import sys
import heapq
input = sys.stdin.readline
maximum = sys.maxsize

N, M, X = list(map(int, input().split()))
m = [[] for _ in range(N + 1)]

for i in range(M):
    u, v, w = list(map(int, input().split()))
    m[u].append((v, w))


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    cost = [maximum] * (N + 1)
    cost[start] = 0

    while queue:
        node = heapq.heappop(queue)
        if node[0] > cost[node[1]]:
            continue
        for element in m[node[1]]:
            dist = node[0] + element[1]
            if cost[element[0]] > dist:
                cost[element[0]] = dist
                heapq.heappush(queue, (dist, element[0]))
    return cost


from_2_to_all_cost = dijkstra(X)
for i in range(1, N + 1):
    from_2_to_all_cost[i] += dijkstra(i)[X]
print(max(from_2_to_all_cost[1:]))
'''

import sys
import heapq
input = sys.stdin.readline
maximum = sys.maxsize

N, M, X = list(map(int, input().split()))
m1 = [[] for _ in range(N + 1)]
m2 = [[] for _ in range(N + 1)]

for i in range(M):
    u, v, w = list(map(int, input().split()))
    m1[u].append((v, w))
    m2[v].append((u, w))


def dijkstra(m, start):
    queue = []
    heapq.heappush(queue, (0, start))
    cost = [maximum] * (N + 1)
    cost[start] = 0

    while queue:
        node = heapq.heappop(queue)
        if node[0] > cost[node[1]]:
            continue
        for element in m[node[1]]:
            dist = node[0] + element[1]
            if cost[element[0]] > dist:
                cost[element[0]] = dist
                heapq.heappush(queue, (dist, element[0]))
    return cost


from_2_to_all_cost = dijkstra(m1, X)
to_2_cost = dijkstra(m2, X)
for i in range(1, N + 1):
    from_2_to_all_cost[i] += to_2_cost[i]
print(max(from_2_to_all_cost[1:]))
