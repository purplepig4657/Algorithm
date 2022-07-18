"""
Baekjoon 13904 과제

"""

import sys
input = sys.stdin.readline

N = int(input())
assignment = [list(map(int, input().split())) for _ in range(N)]
assignment.sort(reverse=True, key=lambda x: (x[1], -x[0]))

assign = [False] * 1001
answer = 0

for a in assignment:
    day = a[0]
    while assign[day]:
        day -= 1
    if day != 0:
        assign[day] = True
        answer += a[1]

print(answer)
