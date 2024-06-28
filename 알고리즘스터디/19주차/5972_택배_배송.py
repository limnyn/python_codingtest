# https://www.acmicpc.net/problem/5972
'''
[문제]
1부터 N까지 도달하기 위한 최소 비용

[입력]
1 <= N <= 50000
1 <= M <= 50000
0 <= C_i <= 1000

N을 노드, M을 간선, C_i를 비용이라고 할 때
비용이 0 이상이기 때문에 다익스트라 알고리즘 적용 가능

다익스트라 알고리즘을 통해 1에서 출발해 모든 노드까지의 최단거리를 계산하여
1->N까지 최단거리를 구할 수 있다.
'''
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

def dijkstra(start, end):
    distance = [float('inf')] * n
    distance[start] = 0
    hq = [(0, 0)]

    while hq:
        dist, node = heapq.heappop(hq)
        
        if distance[node] < dist:
            continue

        for next_node, next_dist in graph[node]:
            if distance[next_node] > dist + next_dist:
                distance[next_node] = dist + next_dist
                heapq.heappush(hq, (distance[next_node], next_node))
    
    return distance[end]

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        start, end, cost = map(int, input().split())
        start, end = start-1, end-1
        graph[start].append((end, cost))
        graph[end].append((start, cost))

    print(dijkstra(0, n-1))