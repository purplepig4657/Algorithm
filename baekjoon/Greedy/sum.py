"""
Baekjoon 1132 합

"""

import sys
input = sys.stdin.readline

N = int(input())
nums = [list(input())[:-1] for _ in range(N)]
alphabet = [[0, False] for _ in range(10)]

for num in nums:
    for i in range(len(num)):
        if i == 0:
            alphabet[ord(num[i]) - 65][1] = True
        alphabet[ord(num[i]) - 65][0] += 10 ** (len(num) - i - 1)

alphabet.sort(key=lambda x: -x[0])
while alphabet[9][1]:
    for i in range(8, -1, -1):
        if not alphabet[i][1]:
            tmp = alphabet[i]
            del alphabet[i]
            alphabet.append(tmp)
            break
answer = 0
for i in range(10):
    answer += alphabet[i][0] * (9 - i)

print(answer)
