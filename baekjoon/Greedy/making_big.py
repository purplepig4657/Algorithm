"""
Baekjoon 2812 크게 만들기

"""

from collections import deque

N, K = list(map(int, input().split()))
number = list(map(int, list(input())))
s = deque()

s.append(number[0])
for i in range(1, N):
    if number[i] > s[len(s) - 1]:
        while s and number[i] > s[len(s) - 1] and K > 0:
            s.pop()
            K -= 1
    s.append(number[i])


if K > 0:
    for _ in range(K):
        s.pop()
while s:
    print(s.popleft(), end='')
