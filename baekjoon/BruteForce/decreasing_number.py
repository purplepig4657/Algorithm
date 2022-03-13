"""
Baekjoon 1038 감소하는 수

"""

import sys
input = sys.stdin.readline

N = int(input())


def nth_number(num, n):
    return int((num / 10 ** (n - 1)) % 10)


def is_valid(n):
    m = len(str(n))
    for i in range(1, m):
        if nth_number(n, i) >= nth_number(n, i + 1):
            return i
    return -1


def increase(n):
    n += 1
    while True:
        m = is_valid(n)
        if m < 0:
            break
        n += 10 ** m
        n -= (10 ** (m - 1)) * nth_number(n, m)
    return n


answer = 0
count = 0

if N > 1022:
    print(-1)
    exit()

while True:
    if count >= N:
        break
    answer = increase(answer)
    count += 1

print(answer)
