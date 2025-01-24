# https://www.acmicpc.net/problem/2211
"""
[문제]
복구 시 조건
1. 최소 개수의 회선만을 복구해야 한다.
2. 슈퍼 컴퓨터가 다른 컴퓨터들과 최소 시간에 통신해야 한다
3. 슈퍼 컴퓨터는 1번 노드

[입력]
1 <= N <= 1000

[접근]
다익스트라
    1. 1번노드에서 모든 노드까지의 최단 경로를 구하고
    2. 최단 경로를 구성하는 간선들을 출력하면 된다.

"""
import sys, heapq
def input(): return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        src, dst, cost = map(int,input().split())
        graph[src].append([dst,cost])
        graph[dst].append([src, cost])
    
    # 입력 예외 처리
    if n == 1:
        print(0)
        exit()

    
    
    # 다익스트라 연산
    trace = [0] * (n + 1) 
    hq = []
    distance = [float("inf")] * (n + 1)
    distance[1] = 0
    heapq.heappush(hq, (0, 1))

    while hq:
        cost, node = heapq.heappop(hq)
        
        if distance[node] < cost:
            continue
        
        for next, next_cost in graph[node]:
            if distance[next] > cost + next_cost:
                distance[next] = cost + next_cost
                heapq.heappush(hq, (distance[next], next))

                # 간선 추적 trace[현재노드] = 이전노드
                trace[next] = node

    print(n - 1) # 간선 수
    for i in range(2, n + 1):
        print(trace[i], i)

        
