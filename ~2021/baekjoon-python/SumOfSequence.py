from math import ceil

N, L = list(map(int, input().split()))

answer = []

for i in range(L, 101):
    if N % i == 0 and i % 2 == 1:
        tf = True
        for j in range(int(N / i) - int(i / 2), int(N / i) + int(i / 2) + 1):
            if j >= 0:
                answer.append(j)
            else:
                answer = []
                tf = False
                break
        if tf:
            break
    if (N / i) % 1 == 0.5 and i % 2 == 0:
        tf = True
        for j in range(ceil(N / i) - int(i / 2), int(N / i) + int(i / 2) + 1):
            if j >= 0:
                answer.append(j)
            else:
                answer = []
                tf = False
                break
        if tf:
            break

if len(answer) == 0:
    print(-1)

for i in answer:
    print(str(i) + " ", end="")
