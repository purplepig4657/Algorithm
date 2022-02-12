input()
c = list(map(int, input().split()))
input()
m = list(map(int, input().split()))

import time

start = time.time()

cm = max(c)
cr = [0] * (cm + 1)
m.sort()
m = list(reversed(m))

if max(m) > cm:
    print(-1)
    exit()

for i in c:
    cr[i] += 1

a = 0

while len(m) != 0:
    cc = cr.copy()
    for i in range(len(cc) - 1, -1, -1):
        if cc[i] != 0:
            for j in range(len(m)):
                if m[j] <= i:
                    cc[i] -= 1
                    m.pop(j)
                    break
    a += 1

print(a)
print(time.time() - start)
