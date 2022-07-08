# 입력 조건
#     첫째 줄에 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C가 주어진다.(1<= N <= 30000, 1 <= M <= 200000,1 <= C <= N)
#     둘째 줄부터 M + 1번째 줄에 걸쳐서 통로에 대한 정보 X, Y, Z가 주어진다. 
#     이는 특정 도시 X에서 다른 특정 도시 Y로 이어지는 통로가 있으며, 메시지가 전달되는 시간이 Z라는 의미다.(1 <= X, Y <= N, 1 <= Z <= 1000)

# 출력 조건
#     첫째 줄에 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 공백으로 구분하여 출력한다.

# 입력 예시
#     3 2 1
#     1 2 4
#     1 3 2

# 출력 예시
#     2 4

# 다익스트라로 C에서 출발, -1이 아닌것의 갯수를 출력하고 그중의 max값 출력


import heapq
import sys

input = sys.stdin.readline
INF = int(1e9) #무한으 의미하는 값으로 10억을 설정

n, m, start = map(int, input().split())
graph = [[] for i  in range(n+1)]
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 ㅗㄴ드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)
result = [x for x in distance if x >= 0 and x<= 1000]
print(len(result)-1, max(result))


