"""
Baekjoon 1715 카드 정렬하기

"""

import sys
import heapq
input = sys.stdin.readline

N = int(input())
card = []

for i in range(N):
    heapq.heappush(card, int(input()))

answer = 0
while len(card) != 1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    answer += a + b
    heapq.heappush(card, a + b)

print(answer)
