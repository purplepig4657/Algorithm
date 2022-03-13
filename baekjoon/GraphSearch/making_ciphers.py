"""
Baekjoon 1759 암호 만들기

"""

import sys
input = sys.stdin.readline

C, L = list(map(int, input().split()))
chars = list(map(ord, input().split()))
chars.insert(0, 0)
chars.sort()

visited = [False] * (L + 1)
seq = [0] * (C + 1)
vowels = [97, 101, 105, 111, 117]


def is_valid(seq):
    vowels_count = 0
    for i in seq:
        if i in vowels:
            vowels_count += 1
    if vowels_count != 0 and len(seq) - vowels_count > 2:
        return True
    return False


def dfs(depth, seq):
    arr = []
    if depth == C:
        if not is_valid(seq):
            return
        for i in seq[1:]:
            print(f"{chr(i)}", end='')
        print()
        return
    for i in range(1, L + 1):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            seq[depth + 1] = chars[i]
            dfs(depth + 1, seq)
    for i in arr:
        visited[i] = False


for i in range(1, L + 1):
    if not visited[i]:
        visited[i] = True
        seq[1] = chars[i]
        dfs(1, seq)
