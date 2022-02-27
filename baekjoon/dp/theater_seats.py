"""
Baekjoon 2302 극장 좌석

"""


def fibonacci(n):
    if n == 0:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


if __name__ == '__main__':
    N = int(input())
    M = int(input())
    vip = [0] * (M + 1)
    for i in range(1, M + 1):
        vip[i] = int(input())
    vip.append(N + 1)

    answer = 1
    for i in range(1, M + 2):
        answer *= fibonacci(vip[i] - vip[i - 1] - 1)

    print(answer)
