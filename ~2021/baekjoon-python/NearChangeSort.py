N = int(input())
A = list(map(int, input().split()))
S = int(input())

As = sorted(A)
As.reverse()

for i in range(N):
    if S == 0:
        break
    for j in range(len(As)):
        d = A.index(As[j]) - i
        p = A.index(As[j])
        if d <= S:
            S -= d
            tmp = As[j]
            for k in range(d):
                A[p - k] = A[p - k - 1]
            A[i] = tmp
            As.remove(tmp)
            break

for i in A:
    print(str(i) + " ", end="")
