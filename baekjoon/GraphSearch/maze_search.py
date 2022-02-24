"""
Baekjoon 2178 미로 탐색

"""

if __name__ == '__main__':
    N, M = list(map(int, input().split()))
    m = [[0] * M for _ in range(N)]

    for i in range(N):
        tmp = input()
        for j in range(M):
            m[i][j] = int(tmp[j])

    queue = list()
    move_ref = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue.append((0, 0))
    m[0][0] = 0
    answer = 1
    count = len(queue)
    breaker = False

    while queue:
        if count > 0:
            position = queue.pop(0)
            count -= 1
            for move in move_ref:
                x = position[1] + move[1]
                y = position[0] + move[0]
                if x == M - 1 and y == N - 1:
                    breaker = True
                    break
                if 0 <= x < M and 0 <= y < N and m[y][x] == 1:
                    m[y][x] = 0
                    queue.append((y, x))
            if breaker:
                answer += 1
                break
        else:
            count = len(queue)
            answer += 1


print(answer)
