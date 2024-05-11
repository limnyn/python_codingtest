# https://www.acmicpc.net/problem/1504
'''
[문제]
    1 -> A, B 정점 방분 -> N 정점
    해당 노드들을 방문하는 '최단 경로'를 찾기

[조건]
    2 <= N <= 800
    0 <= E <= 200,000
    "무방향" 그래프
    
[접근]
    
    "다익스트라 알고리즘 선택"
         (200,000 + 800log800) * 3
    1.
        1, A, B에 대해서 다익스트라 알고리즘을 3번 수행한다
    
    2.
        1-A-B-N 경로와 1-B-A-N 경로 중 최소값을 출력한다.

    다익스트라 알고리즘
        다익스트라 알고리즘

        1. distance(최단거리) 정보를 초기화한다.
        2. 시작 노드에서 시작 노드까지 거리는 0

        3. 시작 노드를 최소 힙에 넣는다.

        4. 힙이 빌 때 까지 
            while min_heap:
                cost, destination = heapq.heappop(min_heap)

                if distance[destination] < cost:
                    continue

                for node in graph[destination]:
                    destination_dist = cost + node[1]

                    if distance[node[0]] >= destination_dist:
                        distance[node[0] = destination_dist
                        heapq.heappush(min_heap, (destination_dist, node[0]))

'''
import sys, heapq
input = sys.stdin.readline


def dijkstra(start_node):
    global distance
    distance = [float('inf')] * n
    distance[start_node] = 0
    min_heap = []
    heapq.heappush(min_heap, (0, start_node))

    
    while min_heap:
        cost, destination = heapq.heappop(min_heap)

        if distance[destination] < cost:
            continue

        for node in graph[destination]:
            destination_dist = cost + node[1]
            
            if distance[node[0]] > destination_dist:
                distance[node[0]] = destination_dist
                heapq.heappush(min_heap, (destination_dist, node[0]))
            


def get_start_a_b_n_distance():
    result = -1

    dijkstra(0)
    start_to_a = distance[a]
    start_to_b = distance[b]
    if start_to_a == float('inf') or start_to_b == float('inf'):
        return result
    
    dijkstra(a)
    a_to_b = distance[b]
    a_to_n = distance[n-1]
    
    dijkstra(b)
    b_to_a = distance[a]
    b_to_n = distance[n-1]
    if a_to_n == float('inf') or b_to_n == float('inf'):
        return result
    
    start_a_b_n = start_to_a + a_to_b + b_to_n
    start_b_a_n = start_to_b + b_to_a + a_to_n
    
    result = min(start_a_b_n, start_b_a_n)
    return result
    




if __name__ == "__main__":
    n, e = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(e):
        start, end, cost = map(int, input().split())
        # 인덱스 0~N-1 로 접근하기 위해
        graph[start-1].append((end-1, cost))
        graph[end-1].append((start-1, cost))
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    distance = []
    print(get_start_a_b_n_distance())


    


    
    

