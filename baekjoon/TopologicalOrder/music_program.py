"""
Baekjoon 2623 음악프로그램

"""

from collections import deque

N, M = list(map(int, input().split()))
pd = [list(map(int, input().split()))[1:] for _ in range(M)]

G = [[] for _ in range(N + 1)]
degree = [0 for _ in range(N + 1)]

for priority in pd:
    last_team = -1
    for team in priority:
        if last_team == -1:
            last_team = team
        else:
            G[last_team].append(team)
            degree[team] += 1
            last_team = team


zero_degree_nodes = []
for i in range(1, N + 1):
    if degree[i] == 0:
        zero_degree_nodes.append(i)

if len(zero_degree_nodes) == 0:
    print(0)
    exit(0)

visited = [False for _ in range(N + 1)]
current = [False for _ in range(N + 1)]


def is_cycle_exist(start_node):
    if visited[start_node]:
        return
    
    visited[start_node] = True
    
    for adjacent_node in G[start_node]:
        if current[adjacent_node]:
            print(0)
            exit(0)
        current[adjacent_node] = True
        is_cycle_exist(adjacent_node)
        current[adjacent_node] = False


answer = []

def topological_sort():
    queue = deque()
    for zero_degree_node in zero_degree_nodes:
        queue.append(zero_degree_node);
        degree[zero_degree_node] = -1
    while queue:
        node = queue.popleft()
        answer.append(node)
        for adjacent_node in G[node]:
            degree[adjacent_node] -= 1        
        for i in range(1, N + 1):
            if degree[i] == 0:
                degree[i] = -1
                queue.append(i)


for zero_degree_node in zero_degree_nodes:
    is_cycle_exist(zero_degree_node)

topological_sort()

for num in answer:
    print(num)

