# https://www.acmicpc.net/problem/11725

"""
루트 노드를 1번이라 가정
1. 연결리스트로 모든 노드 연결
2. 1번 노드 부터 bfs 탐색하며 각 노드의 부모를 기록
3. 출력
"""
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    
    graph = [[] for _ in range(n + 1)]
    parent = [0] * (n + 1)
    
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[b].append(a)
        graph[a].append(b)
    
    
    visited = [False] * (n + 1)
    visited[1] = True    
    dq = deque([1])
    
    while dq:
        node = dq.popleft()
        
        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                parent[next] = node
                dq.append(next)
    
    for i in range(2, n + 1):
        print(parent[i])
        
    
        
    