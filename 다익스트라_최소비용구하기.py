# https://www.acmicpc.net/problem/1916

'''
다익스트라 알고리즘 이란

현재 그룹에 대해
    현재 그룹에서 시작해서 그룹이 아닌 곳으로 가는 간선 들에 대해 최소 힙에 저장하고
    
    현재 그룹이 아닌 곳에 대한 거리 중 가장 가까운 곳을 현재 그룹에 넣고
    새로 들어오는 노드들에 대해서 해당 노드들에 대해 현재 그룹이 아닌 것에 대해 간선을 넣어준다

    반복

    결과적으로 시작점에서부터 모든 것에 대해 거리가 구해진다
현재 그룹이 아닌 것 중 
'''




import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n)]
for _ in range(m):
    s, e, v = map(int, input().split())
    graph[s-1].append((e-1, v))

s, e = map(int, input().split())
s -= 1
e -= 1
for g in graph:
    print(g)

costs = [1e9]* n

costs[s] = 0

group = [False] * n
group[s] = True

dijkstra = []
for end, cost in graph[s]:
    if group[end] == False:
        heapq.heappush(dijkstra, (cost, end, s))
    
print(dijkstra)

while dijkstra:
    cost, end, start = heapq.heappop(dijkstra)
    if group[end] == False:
        group[end] = True
        for e, cost in graph[end]:
            
            heapq.heappush(dijkstra, (cost, e, end))
    costs[end] = min(costs[end], costs[start] + cost)



