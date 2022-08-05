"""
Baekjoon 1826 연료 채우기

"""

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
fuel_info = []

for _ in range(N):
    a, b = list(map(int, input().split()))
    fuel_info.append((a, b))

L, P = list(map(int, input().split()))

fuel_info.sort(key=lambda x: (x[0], -x[1]))

current_fuel = P
heap = []
answer = 0

for i in range(N):
    if current_fuel >= L:
        break
    else:
        while current_fuel < fuel_info[i][0] and len(heap) > 0:
            current_fuel -= heappop(heap)
            answer += 1
    if current_fuel >= fuel_info[i][0]:
        heappush(heap, -fuel_info[i][1])


while current_fuel < L and len(heap) > 0:
    current_fuel -= heappop(heap)
    answer += 1

if current_fuel < L:
    print(-1)
else:
    print(answer)
