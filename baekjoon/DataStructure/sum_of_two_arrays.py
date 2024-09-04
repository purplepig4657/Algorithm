"""
Baekjoon 2143 두 배열의 합

"""

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

sum_of_array_A = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    sum_of_array_A[0][i] = sum_of_array_A[0][i - 1] + A[i - 1];


hash_table = dict()


for i in range(1, n + 1):
    for j in range(i, n + 1):
        sum_of_array_A[i][j] = sum_of_array_A[i - 1][j] - sum_of_array_A[i - 1][i - 1]
        if hash_table.get(sum_of_array_A[i][j]) is not None:
            hash_table[sum_of_array_A[i][j]] += 1
        else:
            hash_table[sum_of_array_A[i][j]] = 1

sum_of_array_B = [[0] * (m + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    sum_of_array_B[0][i] = sum_of_array_B[0][i - 1] + B[i - 1]

answer = 0

for i in range(1, m + 1):
    for j in range(i, m + 1):
        sum_of_array_B[i][j] = sum_of_array_B[i - 1][j] - sum_of_array_B[i - 1][i - 1]
        if hash_table.get(T - sum_of_array_B[i][j]) is not None:
            answer += hash_table[T - sum_of_array_B[i][j]]

print(answer)

