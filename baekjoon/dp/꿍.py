"""
Baekjoon 9507 Generations of Tribbles

"""

import sys
input = sys.stdin.readline


def koongbonacci(n):
    꿍 = [0] * (n + 4)
    꿍[0] = 꿍[1] = 1
    꿍[2] = 2
    꿍[3] = 4
    for i in range(4, n + 1):
        꿍[i] = 꿍[i - 1] + 꿍[i - 2] + 꿍[i - 3] + 꿍[i - 4]
    return 꿍[n]


t = int(input())
for i in range(t):
    print(koongbonacci(int(input())))
