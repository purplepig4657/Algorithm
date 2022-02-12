import math
from itertools import combinations

b = [1, 4, 3, 4, 4]

print(4 in b)
print("*" * 10)

b.pop(1)
print(b)

for i in range(10, 0, -1):
    print(i, end='')

print()
x = [1, 2, 3]
y = [1, 2, 3, 4]
x.extend(y)
print(x)

z = [1, 2, 3]
zz = z[0:2].extend(y)
print(z[0:1])

print(type(list(combinations([1, 2, 3, 4], 2))[0]))
print(set(list(combinations(['a', 'b', 'c', 'd'], 2))[0]))


def combination(array: list, depth: int) -> list:
    all_set = []
    if depth == 0:
        return []
    else:
        for i in range(len(array) - depth + 1):
            tmp = array[i:i + 1]
            tmp.extend(combination(array[i + 1:], depth - 1))
            if depth == 1:
                all_set.append(tmp)
            else:
                for j in range(1, len(tmp)):
                    t = tmp[j]
                    t.insert(0, tmp[0])
                    all_set.append(t)
    return all_set

print("Hello")
