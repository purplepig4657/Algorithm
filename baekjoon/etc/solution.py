"""
Baekjoon 2467 용액

"""

import sys
input = sys.stdin.readline

N = int(input())
solutions = list(map(int, input().split()))

start = 0
end = N - 1
value = abs(solutions[start] + solutions[end])
answer = [solutions[start], solutions[end]]
while start < end:
    v = solutions[start] + solutions[end]
    if value > abs(v):
        answer = [solutions[start], solutions[end]]
        value = abs(v)
    if 0 < v:
        end -= 1
    else:
        start += 1

print(*answer)
