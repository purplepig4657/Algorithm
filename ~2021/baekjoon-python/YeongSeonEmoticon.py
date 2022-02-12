S = int(input())
d = [i for i in range(S + 1)]

for i in range(2, S + 1):
    for j in range(i + 1, S + 1):
        if j % i == 0:
            m = j // i
        else:
            m = j // i + 1
        d[j] = min(d[j], d[i] + (i * m - j) + m)

print(d[S])
