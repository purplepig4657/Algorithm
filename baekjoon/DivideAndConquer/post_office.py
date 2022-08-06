"""
Baekjoon 2141 우체국

"""

# 정렬, 이분탐색 풀이
import sys
input = sys.stdin.readline

N = int(input())

tmp = [list(map(int, input().split())) for _ in range(N)]
tmp.sort(key=lambda x: x[0])

X = [0] * N
A = [0] * N

for i in range(N):
    X[i] = tmp[i][0]
    A[i] = tmp[i][1]


def distance(n):
    result = 0
    for i in range(N):
        result += abs(X[n] - X[i]) * A[i]
    return result


if N <= 2:
    answer = 0
    dist = sys.maxsize
    for i in range(N):
        if distance(i) < dist:
            dist = distance(i)
            answer = i
    print(X[answer])
    exit()


start = 0
end = N - 1
mid = (start + end) // 2

while start <= end:
    mid = (start + end) // 2
    left = distance(mid - 1)
    right = distance(mid + 1)
    middle = distance(mid)
    if middle <= left and middle <= right:
        break
    if right < left:
        start = mid + 1
    else:
        end = mid - 1

dist = distance(mid)
for i in range(mid - 1, - 1, -1):
    if dist < distance(i):
        break
    mid = i
print(X[mid])

""" 그리디, 내 풀이 X
import sys
input = sys.stdin.readline

N = int(input())

po = [list(map(int, input().split())) for _ in range(N)]
po.sort(key=lambda x: x[0])

middle = round(sum(p for _, p in po) / 2)

ac = 0
for i, p in po:
    ac += p
    if ac >= middle:
        print(i)
        break
"""
