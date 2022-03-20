"""
Baekjoon 1629 곱셈

"""

A, B, C = list(map(int, input().split()))

answer = A % C
dp = [0] * 32
dp[0] = answer
count = 0
c = 1
while c != B:
    if 2 ** (count + 1) < B:
        answer *= answer % C
        answer %= C
        count += 1
        c *= 2
        dp[count] = answer
    else:
        dist = B - c
        a = 0
        while 2 ** a <= dist:
            a += 1
        a -= 1
        answer *= dp[a] % C
        answer %= C
        c += 2 ** a

print(answer % C)
