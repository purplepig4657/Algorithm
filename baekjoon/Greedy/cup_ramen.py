"""
Baekjoon 1781 컵라면

"""

import sys
import heapq
input = sys.stdin.readline

N = int(input())
homework = [list(map(int, input().split())) for _ in range(N)]
heap = []

homework.sort(key=lambda x: (x[0], -x[1]))

answer = 0

for w in homework:
    if len(heap) + 1 <= w[0]:
        heapq.heappush(heap, w[1])
        answer += w[1]
    else:
        peek = heap[0]
        if peek < w[1]:
            heapq.heappop(heap)
            heapq.heappush(heap, w[1])
            answer = answer - peek + w[1]

print(answer)
