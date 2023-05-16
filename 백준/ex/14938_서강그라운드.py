# https://www.acmicpc.net/problem/14938
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
cost = list(map(int, input().split()))

graph = [[1e9] * n for _ in range(n)]
for i in range(n):
    graph[i][i] = 0

for _ in range(r):
    node1, node2, weight = map(int, input().split())
    graph[node1 - 1][node2 - 1] = weight
    graph[node2 - 1][node1 - 1] = weight


def floydwashall(graph):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph


graph = floydwashall(graph)

costmax = 0
for i in range(n):
    cost_i = 0
    for j in range(n):
        if graph[i][j] <= m:
            cost_i += cost[j]
    costmax = max(costmax, cost_i)

print(costmax)
