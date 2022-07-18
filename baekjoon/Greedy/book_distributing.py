"""
Baekjoon 9576 책 나눠주기

"""

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = list(map(int, input().split()))
    student = [list(map(int, input().split())) for _ in range(M)]
    book = [False] * (N + 1)

    student.sort(key=lambda x: (-x[0], x[1]))

    answer = 0

    for s in student:
        book_idx = s[1]
        while book_idx >= s[0] and book[book_idx]:
            book_idx -= 1
        if book_idx >= s[0]:
            book[book_idx] = True
            answer += 1

    print(answer)
