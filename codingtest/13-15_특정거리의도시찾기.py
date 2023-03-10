# https://www.acmicpc.net/problem/18352

n, m, k, x = map(int, input().split())


city = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    city[a].append(b)
    
distance = [-1] * (n + 1)
distance[x] = 0

from collections import deque
q = deque([x])
while q:
    now = q.popleft()
    for next_node in city[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)
            
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True
if check == False:
    print(-1)
        
# n, m, k, x = map(int, input().split())


# city = [[] for _ in range(n)]
# for i in range(m):
#     a, b = map(int, input().split())
#     city[a-1].append(b-1)

# from collections import deque
# # BFS 메서드 정의
# def bfs(graph, start):
#     visited = [False] * n    
#     queue = deque([start])
#     visited[start[0]] = True
#     result = []
#     while queue:
#         v, level = queue.popleft()
#         if level==k:
#             result.append(v+1)
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append([i, level+1])
#                 visited[i] = True
    
#     if len(result) == 0:
#         print(-1)
#     else:
#         result.sort()
#         for r in result:
#             print(r)


# bfs(city, [0,0])