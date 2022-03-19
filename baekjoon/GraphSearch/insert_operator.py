"""
Baekjoon 14888 연산자 끼워넣기

"""

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))
operators = list(map(int, input().split()))
operator_list = []
for i in range(4):
    for j in range(operators[i]):
        operator_list.append(i)

visited = [False] * (N - 1)
operator_seq = [-1] * (N - 1)
answer_max = -sys.maxsize
answer_min = sys.maxsize


def calculate(operator_seq):
    result = seq[0]
    for i in range(N - 1):
        if operator_seq[i] == 0:
            result += seq[i + 1]
        elif operator_seq[i] == 1:
            result -= seq[i + 1]
        elif operator_seq[i] == 2:
            result *= seq[i + 1]
        else:
            if result < 0:
                result = -(abs(result) // seq[i + 1])
            else:
                result //= seq[i + 1]

    return result


def dfs(depth, operator_seq):
    global answer_max
    global answer_min
    if depth == N - 1:
        result = calculate(operator_seq)
        answer_max = max(answer_max, result)
        answer_min = min(answer_min, result)
        return
    for i in range(N - 1):
        if not visited[i]:
            visited[i] = True
            operator_seq[depth] = operator_list[i]
            dfs(depth + 1, operator_seq)
            visited[i] = False


for i in range(N - 1):
    visited[i] = True
    operator_seq[0] = operator_list[i]
    dfs(1, operator_seq)
    visited[i] = False

print(answer_max)
print(answer_min)
