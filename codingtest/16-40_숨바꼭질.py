# 동빈이는 숨바꼭질을 하면서 술래로부터 잡히지 않도록 숨을 곳을 찾고 있습니다.
# 동빈이는 1 ~ N번까지의 헛간 중에서 하나를 골라 숨을 수 있으며, 술래는 항상 1번 헛간에서 출발합니다.
# 전체 맵에는 총 M개의 양방향 통로가 존재하며, 하나의 통로는 서로 다른 두 헛간을 연결합니다.
# 또한 전체 맵은 항상 어떤 헛간에서 다른 어떤 헛간으로 도달이 가능한 형태로 주어집니다.
# 동빈이는 1번 헛간으로부터 최단 거리가 가장 먼 헛간이 가장 안전하다고 판단하고 있습니다. 이때 최단거리의 의미는 지나야 하는 길의 최소 개수를 의미합니다.
# 동빈이가 숨을 헛간의 번호를 출력하는 프로그램을 작성하세요.

# 입력 조건
#     첫째 줄에는 N과 M이 주어지며, 공백으로 구분합니다.
#     이후 M개의 줄에 걸쳐서 서로 연결된 두 헛간 A와 B의 번호가 공백으로 구분되어 주어집니다.
#     (1 <= A, B <= N)
    
# 출력 조건
#     첫 번째는 숨어야 하는 헛간 번호를(만약 거리가 같은 헛간이 여러 개면 가장 작은 헛간 번호를 출력합니다).
#     두 번째는 그 헛간까지의 거리를, 세 번째는 그 헛간과 같은 거리를 갖는 헛간의 개수를 출력해야 합니다.
    
# 입력 예시
# 6 7
# 3 6
# 4 5
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2
    
# 출력 예시
#     4 2 3


INF = 1e9
n, m = map(int, input().split())
start = 1
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

import heapq

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: #큐가 비어있지 않다면
        # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(start)

# 최단 거리가 가장 먼 노드 번호(동빈이가 숨을 헛간의 번호)
max_node = 0 
# 가장 먼노드의 최단거리
max_distance = 0
# 동일한 최단거리인 노드들
result = []

for i in range(1, n+1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)
print(max_node, max_distance,len(result))

# print(graph)
# result = dijkstra(graph, 1)
# print(result)
# # print(graph)




