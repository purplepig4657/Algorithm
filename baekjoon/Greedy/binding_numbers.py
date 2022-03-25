"""
Baekjoon 1744 수 묶기

"""

import sys
input = sys.stdin.readline

N = int(input())
positive = []
negative = []
for i in range(N):
    n = int(input())
    if n >= 0:
        positive.append(n)
    else:
        negative.append(n)

positive.sort(reverse=True)
negative.sort()

answer = 0

while len(positive) > 1:
    if positive[0] != 0 and positive[1] != 0 and positive[0] != 1 and positive[1] != 1:
        answer += positive[0] * positive[1]
        for _ in range(2):
            del positive[0]
    else:
        break

while len(negative) > 1:
    answer += negative[0] * negative[1]
    for _ in range(2):
        del negative[0]

if len(negative) >= 1:
    if len(positive) > 0 and min(positive) == 0:
        del negative[0]
    else:
        answer += negative[0]

if len(positive) >= 1:
    answer += sum(positive)

print(answer)
