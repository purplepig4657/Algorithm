"""
Baekjoon 12904 A와 B

"""

from collections import deque

S = list(input())
T = deque(list(input()))

reverse = False
for _ in range(len(T) - len(S)):
    if not reverse:
        c = T.pop()
    else:
        c = T.popleft()
    if c == 'B':
        reverse = not reverse

for i in range(len(S)):
    if not reverse:
        c = T.popleft()
    else:
        c = T.pop()
    if S[i] != c:
        print(0)
        exit()
print(1)
