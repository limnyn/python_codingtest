# https://www.acmicpc.net/problem/2606

n = int(input())
m = int(input())

graph = [[] for _ in range(n)]
visited = [0] * n
for i in range(m):
    s, e = map(int, input().split())
    graph[s - 1].append(e - 1)
    graph[e - 1].append(s - 1)


from collections import deque

dq = deque()
dq.append(0)

while dq:
    start = dq.popleft()
    for edge in graph[start]:
        if not visited[edge]:
            visited[edge] = 1
            dq.append(edge)

if m == 0:
    print(0)
else:
    print(sum(visited) - 1)
