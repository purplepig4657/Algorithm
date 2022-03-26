"""
Baekjoon 2457 공주님의 줭원

"""

import sys
input = sys.stdin.readline

N = int(input())
flowers = [list(map(int, input().split())) for _ in range(N)]

flowers.sort(key=lambda x: (x[0], x[1], x[2], x[3]))


def compare(x1, x2):
    x1_compute = x1[0] * 100 + x1[1]
    x2_compute = x2[0] * 100 + x2[1]
    return x1_compute > x2_compute


start = [3, 1]
end = [0, 0]
answer = 0

i = 0
while i < len(flowers):
    if not compare([12, 1], end):
        break
    if not compare([flowers[i][0], flowers[i][1]], start):
        if not compare(end, [flowers[i][2], flowers[i][3]]):
            end = [flowers[i][2], flowers[i][3]]
    elif start != end:
        start = [end[0], end[1]]
        answer += 1
        i -= 1
    i += 1

if compare([12, 1], end):
    print(0)
else:
    print(answer + 1)
