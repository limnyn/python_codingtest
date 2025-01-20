# https://www.acmicpc.net/problem/1516
"""
1. 각 건물간 상관관계를 그래프 화
2. 위상정렬
3. 자신의 입력간선 + 자신의 건설 시간의 최대값을 갱신
"""
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()
if __name__ == "__main__":
    n = int(input())
    
    times = [0] * (n + 1)
    in_degree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        data = list(map(int, input().split()))
        times[i] = data[0]
        
        for prerequisite in data[1:-1]:
            graph[prerequisite].append(i)
            in_degree[i] += 1
    
    queue = deque()
    result = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)
            result[i] = times[i]
            
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            in_degree[next_node] -= 1
            result[next_node] = max(result[next_node], result[node] + times[next_node])
            if in_degree[next_node] == 0:
                queue.append(next_node)
    
    for i in range(1, n + 1):
        print(result[i])     
    
    

        
            