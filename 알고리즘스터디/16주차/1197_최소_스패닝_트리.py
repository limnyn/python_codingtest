# https://www.acmicpc.net/problem/1197
'''
mst 문제

mst 구현 방법
    1. kruskal 방법
        모든 간선을 가중치 기준으로 오름차순 정렬하여 트리 구성
        O(nlogn)
    2. prim 방법
        시작점에서 단계적으로 노드를 추가하는 방식으로 트리 구성
        이진 힙 사용 시 O(ElogV)

    prim 알고리즘으로 mst를 구현해보자
        각 노드에 대해서 인접 간선을 heapq에 push. pop 해서 처리
        

    def prim_mst():
        visited = [False] * v
        start_node = 0 #0번 노드에서 수행
        group_cnt = 0
        result = 0
        group_heap = []
        heapq.heappush(group_heap, (0, 0)) #0번 노드에서 0번 노드까지 비용 0
        
        while group_heap:
            dist, end = heapq.heappop(group_heap)

            if visited[end] == True:
                continue
            
            visited[end] = True
            result += dist
            group_cnt += 1

            for next, cost in graph[end]:
                if visited[next] == False:
                    heapq.heappush(group_heap, (cost, next))

            if group_cnt == v:
                return result
'''
import sys, heapq
input = sys.stdin.readline

def prim_mst():
    visited = [False] * v
    start_node = 0 #0번 노드에서 수행
    group_cnt = 0
    result = 0
    group_heap = []
    heapq.heappush(group_heap, (0, 0)) #0번 노드에서 0번 노드까지 비용 0
    
    while group_heap:
        dist, end = heapq.heappop(group_heap)

        if visited[end] == True:
            continue
        
        visited[end] = True
        result += dist
        group_cnt += 1

        for next, cost in graph[end]:
            if visited[next] == False:
                heapq.heappush(group_heap, (cost, next))

        if group_cnt == v:
            return result

if __name__ == '__main__':
    v, e = map(int, input().split())
    graph = [[] for _ in range(v)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append((b,c))
        graph[b].append((a,c))
    print(prim_mst())

            
            

