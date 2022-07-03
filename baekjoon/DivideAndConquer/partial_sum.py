"""
Baekjoon 1806 부분합

"""

import sys
input = sys.stdin.readline

N, S = list(map(int, input().split()))
seq = list(map(int, input().split()))


def partial_sum(n):
    psum = sum(seq[:n])
    if n == 0:
        return False
    for i in range(n, N):
        if psum >= S:
            return True
        psum += seq[i] - seq[i - n]
    if psum >= S:
        return True
    else:
        return False


def binary_search():
    start = 0
    end = N
    mid = int((start + end) / 2)

    while end - start > 1:
        if partial_sum(mid):
            end = mid
        else:
            start = mid
        mid = int((start + end) / 2)

    return start, end


s, e = binary_search()
s_result = partial_sum(s)
e_result = partial_sum(e)
if not s_result and not e_result:
    print(0)
elif s_result and e_result:
    print(s)
elif s_result:
    print(s)
else:
    print(e)
