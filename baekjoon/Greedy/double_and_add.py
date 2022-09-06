"""
Baekjoon 12931 두 배 더하기

"""

import sys
input = sys.stdin.readline

N = int(input())
B = list(map(int, input().split()))

is_end = [False] * N
for i in range(N):
    if B[i] == 0:
        is_end[i] = True
answer = -1

while False in is_end:
    can_divide = True
    for i in range(N):
        if is_end[i]:
            continue
        if B[i] == 0:
            is_end[i] = True
        if B[i] % 2 == 1:
            answer += 1
            B[i] -= 1
            can_divide = False
    if can_divide:
        for i in range(N):
            B[i] = B[i] // 2
        answer += 1

print(answer if answer > 0 else 0)
