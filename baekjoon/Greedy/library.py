"""
Baekjoon 1461 도서관

"""

N, M = list(map(int, input().split()))
m = list(map(int, input().split()))
m.append(0)
m.sort()

answer = []
i = 0
while m[i] != 0:
    if i % M == 0:
        answer.append(m[i])
    i += 1

i = 0
while m[N - i] != 0:
    if i % M == 0:
        answer.append(m[N - i])
    i += 1

answer = list(map(abs, answer))
print(2 * sum(answer) - max(answer))
