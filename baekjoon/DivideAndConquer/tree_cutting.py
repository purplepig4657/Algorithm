"""
Baekjoon 2805 나무 자르기

"""

import sys
input = sys.stdin.readline
M, H = list(map(int, input().split()))
trees = list(map(int, input().split()))


def cutting_length(height):
    length = 0
    for i in range(M):
        length += max(0, trees[i] - height)
    return length


start = 0
end = max(trees)

while start <= end:
    mid = (start + end) // 2
    length = cutting_length(mid)
    if length == H:
        print(mid)
        exit()
    elif length > H:
        start = mid + 1
    else:
        end = mid - 1

mid = (start + end) // 2
print(mid)
