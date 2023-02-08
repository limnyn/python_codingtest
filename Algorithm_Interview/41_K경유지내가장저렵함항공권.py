# 시작점에서 도착점까지의 가장 저렴한 가격을 계산하되,
# K개의 경유지 이내에 도착하는 가격을 리턴하라.
# 경로가 존재하지 않을 경우 -1을 리턴한다.

n = 3
edge = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
K = 0
import heapq
import collections
def  findCheapestPrice(flights, src, K):
    graph = collections.defaultdict(list)
    
    for u, v, w in flights:
        graph[u].append((v,w))
    # 큐 변수 : [(가격, 정점, 남은 가능 경유지 수)]
    k = 0
    Q = [(0, src, K)]
    

    # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k <= K:
            k+=1
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(Q, (alt, v, k))

    # 모든 노드의 최단 경로 존재 여부 판별
 
    return -1
print(findCheapestPrice(edge,src,K))