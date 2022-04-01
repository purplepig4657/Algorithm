"""
Baekjoon 2212 센서

"""

import sys
input = sys.stdin.readline

N, K = int(input()), int(input())
sensor = list(map(int, input().split()))

sensor.sort()
dsensor = []
for i in range(1, N):
    dsensor.append(sensor[i] - sensor[i - 1])

dsensor.sort(reverse=True)
print(sum(dsensor[K - 1:]))
