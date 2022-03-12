"""
Baekjoon 1753 최단경로

"""

'''
import sys
input = sys.stdin.readline
maximum = sys.maxsize

V, E = list(map(int, input().split()))
K = int(input())
min_heap = [(maximum, maximum)] * (V + 1)
min_heap_size = 0


def insert_min_heap(x):
    global min_heap_size
    min_heap_size += 1
    min_heap[min_heap_size] = x

    i = min_heap_size
    while i > 1:
        if min_heap[int(i / 2)][0] > min_heap[i][0]:
            min_heap[i], min_heap[int(i / 2)] = min_heap[int(i / 2)], min_heap[i]
            i = int(i / 2)
        else:
            break


def delete_min_heap():
    global min_heap_size
    min_heap[1], min_heap[min_heap_size] = min_heap[min_heap_size], (maximum, maximum)
    min_heap_size -= 1

    i = 1
    while i * 2 <= min_heap_size:
        if min_heap[i * 2][0] > min_heap[i][0] and min_heap[i * 2 + 1][0] > min_heap[i][0]:
            break
        elif min_heap[i * 2][0] < min_heap[i * 2 + 1][0]:
            min_heap[i], min_heap[i * 2] = min_heap[i * 2], min_heap[i]
            i *= 2
        else:
            min_heap[i], min_heap[i * 2 + 1] = min_heap[i * 2 + 1], min_heap[i]
            i = i * 2 + 1


def pop_min_heap():
    value = min_heap[1]
    delete_min_heap()
    return value


m = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = list(map(int, input().split()))
    m[u].append((v, w))

answer = [maximum] * (V + 1)

insert_min_heap((K, 0))
answer[K] = 0

while min_heap[1] != (maximum, maximum):
    node = pop_min_heap()
    if node[1] > answer[node[0]]:
        continue
    for i in m[node[0]]:
        if answer[i[0]] > i[1] + node[1]:
            insert_min_heap((i[0], i[1] + node[1]))
            answer[i[0]] = i[1] + node[1]

for i in answer[1:]:
    if i == maximum:
        print("INF")
        continue
    print(i)
'''

import sys
import heapq
input = sys.stdin.readline

V, E = list(map(int, input().split()))
K = int(input())
maximum = sys.maxsize

m = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = list(map(int, input().split()))
    m[u].append((v, w))

answer = [maximum] * (V + 1)

queue = []
heapq.heappush(queue, (0, K))
answer[K] = 0

while queue:
    node = heapq.heappop(queue)
    if node[0] <= answer[node[1]]:
        for e in m[node[1]]:
            dist = e[1] + node[0]
            if answer[e[0]] > dist:
                answer[e[0]] = dist
                heapq.heappush(queue, (dist, e[0]))

for i in answer[1:]:
    if i == maximum:
        print("INF")
        continue
    print(i)
