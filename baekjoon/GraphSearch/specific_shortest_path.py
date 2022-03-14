"""
Baekjoon 1504 특정한 최단 경로

"""

import sys
import heapq

input = sys.stdin.readline

N, M = list(map(int, input().split()))

m = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = list(map(int, input().split()))
    m[u].append((v, w))
    m[v].append((u, w))

node1, node2 = list(map(int, input().split()))
maximum = sys.maxsize


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


cost = dijkstra(1)
cost_node1 = dijkstra(node1)
cost_node2 = dijkstra(node2)
node1_to_node2 = cost[node1] + cost_node1[node2] + cost_node2[N]
node2_to_node1 = cost[node2] + cost_node2[node1] + cost_node1[N]

if cost[N] == maximum or cost[node1] == maximum or cost_node1[node2] == maximum:
    print(-1)
elif node1_to_node2 <= node2_to_node1:
    print(node1_to_node2)
else:
    print(node2_to_node1)
