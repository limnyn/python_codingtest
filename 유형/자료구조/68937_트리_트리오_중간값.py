# https://school.programmers.co.kr/learn/courses/30/lessons/68937?language=python3
from collections import deque, defaultdict

def bfs(start, graph, n):
    
    
    dq = deque([])
    distance = [0] * (n + 1)
    visited = [False] * (n + 1)        
    
    dq.append((start, 0))
    visited[start] = True
    
    
    farest_node = 0
    while dq:
        node, dist = dq.popleft()    
        
        for next_node in graph[node]:
            if visited[next_node]:
                continue
                
            visited[next_node] = True
            distance[next_node] = dist + 1
            dq.append((next_node, dist + 1))
        
    farest_node = 0
    farest_node_cnt = 0
    max_dist = max(distance)
    for node in range(1, n + 1):
        if distance[node] == max_dist:
            farest_node = node
            farest_node_cnt += 1
    
    return farest_node, farest_node_cnt, max_dist

def solution(n, edges):
    """
    입출력 예에 따라서
    1. 트리의 지름이 하나인 경우
        가장 먼 거리는 지름, 그 다음으로 먼 거리는 지름 - 1
    2. 트리의 지름이 두개 이상인 경우
        가장 먼 거리는 지름, 지름이 여러개면 그 다음 값도 지름이다
        
    [트리의 지름 구하기]
    1. 특정 노드에서 BFS를 통해 가장 먼 점 A를 구한다.
    2, 가장 먼 점 A에서 BFS를 통해 가장 먼 거리에 있는 노드를 구한다
    3. 만약 가장 먼 거리에 있는 노드가 하나일 때는 다시 해당 지점에서 BFS를 수행해서 이때도 한개라면 지름은 하나
    
    이때 A에서 가장 먼 거리에 있는 노드까지의 거리가 지름이다.
    가장 먼 거리에 있는 노드의 개수가 지름의 개수
    """

    
    graph = defaultdict(list)
    for src, dst in edges:
        graph[src].append(dst)
        graph[dst].append(src)
    
    start_node, _, _ = bfs(1, graph, n)
    farest_node, node_cnt, node_distance = bfs(start_node, graph, n)
    
    if node_cnt == 1:
        farest_node, node_cnt, node_distance = bfs(farest_node, graph, n)
    
    if node_cnt == 1:
        return node_distance - 1
    else:
        return node_distance
    