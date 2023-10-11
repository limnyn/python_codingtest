# https://www.acmicpc.net/problem/1260


n, m, start = map(int, input().split())
start -= 1
graph = [[] for _ in range(n)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s - 1].append(e - 1)
    graph[e - 1].append(s - 1)

visited = [0] * n
result = [start + 1]
visited[start] = 1


def dfs(now):
    graph[now].sort()
    for edge in graph[now]:
        if visited[edge] == 0:
            visited[edge] = 1
            print(edge + 1, end=" ")
            dfs(edge)


from collections import deque


def bfs(start):
    visited = [0] * n
    visited[start] = 1
    dq = deque([graph[start]])
    print(start + 1, end=" ")
    while dq:
        now = dq.popleft()
        for edge in now:
            if visited[edge] == 0:
                visited[edge] = 1
                print(edge + 1, end=" ")
                result.append(edge + 1)
                dq.append(graph[edge])


print(start + 1, end=" ")
dfs(start)
print()
bfs(start)
print()
