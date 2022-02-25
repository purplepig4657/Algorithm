"""
Baekjoon 2011 암호코드

"""

cipher = list(map(int, input()))
cipher.insert(0, 0)
dp = [0 for _ in range(len(cipher))]

dp[0] = 1

if cipher[1] != 0:
    dp[1] = 1

for i in range(2, len(cipher)):
    cipher1 = cipher[i - 1]
    cipher2 = cipher[i]
    cipher1_2 = cipher1 * 10 + cipher2

    if cipher2 != 0:
        dp[i] += dp[i - 1] % 1000000

    if 0 < cipher1_2 <= 26 and cipher1 != 0:
        dp[i] += dp[i - 2] % 1000000

print(dp[len(cipher) - 1] % 1000000)
