# 배고파 시발
N = int(input())
answer = 0
a = 1

while True:
    if a * a >= N:
        N = N - (a - 1) * (a - 1)
        a = 0
        answer = answer + 1
    if N == 0:
        break
    if N == 1:
        answer = answer + 1
        break
    a = a + 1

print(answer)
