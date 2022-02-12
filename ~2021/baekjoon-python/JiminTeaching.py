from itertools import combinations


def to_binary(array):
    b = 0
    for a in array:
        b = b + 2 ** (ord(a) - ord('a'))
    return b + base


N, K = list(map(int, input().split()))
K = K - 5
wl = []

for i in range(N):
    wl.append(set(input()[4:-4]) - {'a', 'n', 't', 'i', 'c'})

base = 532741  # 2 ** 0 + 2 ** 13 + 2 ** 19 + 2 ** 8 + 2 ** 2

awl: set = {''}
for s in wl:
    awl = awl | s
awl.remove('')

for i in range(len(wl)):
    wl[i] = to_binary(wl[i])

if K < 0:
    print(0)
    exit()
elif len(awl) <= K or K == 21:
    print(N)
    exit()

answer = 0
for s in combinations(awl, K):
    count = 0
    for i in wl:
        if to_binary(s) & i == i:
            count = count + 1
    answer = max(answer, count)

print(answer)
