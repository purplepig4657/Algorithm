import sys
from collections import deque


def bfs(graph, start_node, N) -> int:
    score = 0
    queue = deque()
    queue.append((start_node, 0))
    visited = [False for _ in range(N)]
    visited[start_node] = True
    while queue:
        node, max_value = queue.popleft()
        friend_list = graph[node]
        for friend in friend_list:
            if not visited[friend]:
                queue.append((friend, max_value + 1))
                score = max(score, max_value + 1)
            visited[friend] = True

    return score



if __name__ == '__main__':

    N = int(input())

    graph = [list() for _ in range(N)]

    while True:
        friend1, friend2 = list(map(int, input().split()))

        if friend1 == -1 and friend2 == -1:
            break

        graph[friend1 - 1].append(friend2 - 1)
        graph[friend2 - 1].append(friend1 - 1)

    candidate_list = []
    candidate_score = sys.maxsize

    for friend in range(N):
        score = bfs(graph, friend, N)
        if score < candidate_score:
            candidate_list = [friend + 1]
            candidate_score = score
        elif score == candidate_score:
            candidate_list.append(friend + 1)
        else:
            pass

    print(candidate_score, len(candidate_list))
    candidate_list.sort()
    print(*candidate_list)

