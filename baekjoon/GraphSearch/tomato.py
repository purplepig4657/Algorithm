"""
Baekjoon 7576 토마토

"""

from collections import deque

if __name__ == '__main__':
    M, N = list(map(int, input().split()))

    m = [[0] * M for _ in range(N)]
    deq = deque()

    for i in range(N):
        tmp = list(map(int, input().split(" ")))
        for j in range(M):
            if tmp[j] == 1:
                deq.append((i, j))
            m[i][j] = int(tmp[j])

    move_ref = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    answer = 0
    count = len(deq)

    while deq:
        if count > 0:
            position = deq.popleft()
            count -= 1
            for move in move_ref:
                x = position[1] + move[1]
                y = position[0] + move[0]
                if 0 <= x < M and 0 <= y < N and m[y][x] == 0:
                    deq.append((y, x))
                    m[y][x] = 1

        else:
            count = len(deq)
            answer += 1

    for i in range(N):
        if 0 in m[i]:
            print(-1)
            exit()

    print(answer)
