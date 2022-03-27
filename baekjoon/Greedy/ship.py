"""
Baekjoon 1092 배

"""

import sys
input = sys.stdin.readline

N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)
can_load = [True] * N
answer = 0

while len(boxes) > 0:
    load_count = 0
    for i in range(N):
        if can_load[i]:
            load = False
            for j in range(len(boxes)):
                if cranes[i] >= boxes[j]:
                    del boxes[j]
                    load = True
                    load_count += 1
                    break
            if not load:
                can_load[i] = False
                break
        else:
            break
    if load_count == 0:
        print(-1)
        exit()
    answer += 1

print(answer)
