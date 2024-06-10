# https://www.acmicpc.net/problem/11779

'''
최단'경로'를 추적하는 문제
    -> 다익스트라에서 값을 갱신할 때, 이전 노드를 리스트에 저장하는 방식을 사용
    이전 경로를 저장해 놓고 재귀적으로 추적해 경로를 출력할 수 있다.
    -> trace 함수
'''

import sys, heapq
input = sys.stdin.readline

def dijkstra():
    hq = []
    
    distance[src_city] = 0
    heapq.heappush(hq, (0, src_city))

    before_node[src_city] = src_city

    while hq:
        dist, now = heapq.heappop(hq)

        if distance[now] < dist:
            continue
        for node in graph[now]:
            cost = dist + node[1]

            if cost < distance[node[0]]:
                distance[node[0]] = cost
                before_node[node[0]] = now #값이 갱신될 때 이전 노드를 기록한다.
                heapq.heappush(hq, (cost, node[0]))
    
    trace(dst_city) # 목적지부터 재귀적으로 경로를 추적


    
def trace(src_city):
    '''
    목적지부터 재귀적으로 경로를 추적해서 trace_result 전역 리스트에 삽입
    '''
    if before_node[src_city] == src_city:
        trace_result.append(src_city)
        return
    trace(before_node[src_city])
    trace_result.append(src_city)
    
    



if __name__ == "__main__":
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        src, dst, cost = map(int, input().split())
        src -= 1
        dst -= 1
        graph[src].append((dst, cost))
    src_city, dst_city = map(int, input().split())
    src_city -= 1
    dst_city -= 1

    distance = [float('inf')] * n
    before_node = [-1] * n # 경로 추적을 위해 이전 노드를 기억할 공간
    trace_result = [] # 추적된 경로
    dijkstra()
    
    #결과 출력
    # 1. 출발 도시에서 도착 도시까지 가는데 드는 최소 비용
    print(distance[dst_city])
    # 2. 최소 비용을 갖는경로에 포함되어 있는 도시의 개수
    print(len(trace_result))
    # 3. 최단 경로 출력
    for node in trace_result:
        print(node+1, end=' ')
    print()