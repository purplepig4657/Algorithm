"""
Baekjoon 1916 최소비용 구하기

"""

import sys
import heapq

input = sys.stdin.readline

N, M = int(input()), int(input())

m = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = list(map(int, input().split()))
    m[u].append((v, w))

start, end = list(map(int, input().split()))

queue = []
heapq.heappush(queue, (0, start))
cost = [sys.maxsize] * (N + 1)
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


print(cost[end])
