"""
Baekjoon 1991 트리 순회

"""

import sys
input = sys.stdin.readline

N = int(input())
tree = [(0, 0)] * N

for _ in range(N):
    p, l, r = input().split()
    tree[ord(p) - 65] = (ord(l) - 65, ord(r) - 65)


def traversal(order, node):
    for i in order:
        if i == 0:
            print(chr(node + 65), end='')
        elif i == 1 and tree[node][i - 1] >= 0:
            traversal(order, tree[node][i - 1])
        elif tree[node][i - 1] >= 0:
            traversal(order, tree[node][i - 1])


traversal([0, 1, 2], 0)
print()
traversal([1, 0, 2], 0)
print()
traversal([1, 2, 0], 0)
