# K부터 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산하라.
# 불가능 할 경우 -1을 리턴한다.
# 입력값(u, v, w)는 각각 출발지, 도착지, 소요시간으로 구성되며, 전체 노드의 개수는 N으로 입력받는다.

# 입력
times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2

import heapq
import collections
def  networkDelayTime(times, N, K):
    graph = collections.defaultdict(list)
    
    for u, v, w in times:
        graph[u].append((v,w))
    # 큐 변수 : [(소요시간, 정점)]
    Q = [(0, K)]
    dist = collections.defaultdict(int)

    # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))

    # 모든 노드의 최단 경로 존재 여부 판별
    if len(dist) == N:
        return max(dist.values())
    return -1
print(networkDelayTime(times,N,K))