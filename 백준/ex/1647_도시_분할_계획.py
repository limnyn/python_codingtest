# https://www.acmicpc.net/problem/1647

'''
[문제]
그래프로 된 마을이 존재할 때, 마을을 두 개로 분리한다.
이때, 각 마을의 내부는 최소 비용으로 이어지도록 한다

[조건]
집의 개수 2 <= N <= 100,000
길의 개수 1 <= M <= 1,000,000
길의 유지비 1 <= C <= 1,000

[접근]
각 분리된 마을 안에 있는 임의의 두 집 사이에 경로가 항상 존재해야 한다.
    -> MST, 최소 비용 신장 트리로 이으면 최소 비용으로 마을을 모두 이을 수 있다.

-> 모든 마을을 MST로 연결한 다음, MST 내부의 가장 비용이 큰 간선을 제거하면 두 집합으로 나눠지지 않을까?

'''

import sys, heapq
input = sys.stdin.readline

def prim():
    mst_sum = 0
    mst_connect = [False] * n
    group_cnt = 0
    
    max_edge_in_mst = float('-inf')
    
    hq = []
    heapq.heappush(hq, (0, 0))
    
    while hq:
        dist, now = heapq.heappop(hq)
        max_edge_in_mst = max(max_edge_in_mst, dist)
        
        if mst_connect[now]:
            continue

        mst_sum += dist
        mst_connect[now] = True
        group_cnt += 1
        
        for node in graph[now]:
            if mst_connect[node[0]]:
                continue
            heapq.heappush(hq, (node[1], node[0]))
        
        if group_cnt == n: 
            break
    
    return mst_sum - max_edge_in_mst # MST에서 최대비용 간선 제거


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        src, dst, cost = map(int, input().split())
        src -= 1
        dst -= 1
        graph[src].append((dst, cost))
        graph[dst].append((src, cost))

    print(prim())


