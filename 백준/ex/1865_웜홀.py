# https://www.acmicpc.net/problem/1865
'''
[문제]
    특정 노드 A에서 출발해서 다시 A로 돌아왔을 때 시간이 출발시점보다 이전으로 돌아가는 경우가 있는지 없는지 판별하기

[조건]
   1 <= N <= 500
   1 <= M <= 2500
   1 <= W <= 200

[접근]
    [웜홀을 통과 시 시간이 돌아간다]
    -> 단방향 음의 가중치를 가진 간선이라고 생각하기
    
    [A에서 A로 돌아왔을 때 출발 시점보다 시간이 뒤로 돌아가는 경우]
    -> 특정 음수사이클이 존재하고, A가 음수 사이클에 연결되어 있으면 가능하다.

[음수 사이클 찾기]
    벨만포드를 통해 최단거리를 발견하면 Yes를 출력하고
    이외에는 No를 출력한다.     
'''
import sys
def input(): return sys.stdin.readline().rstrip()

def negative_cycle_checker(start_node):
    distance = [float('inf')] * n
    distance[start_node] = 0
    for _ in range(n - 1):
        for node in range(n):
            if distance[node] == float('inf'):
                continue
            for end, cost in graph[node]:
                if cost < 0:
                    visitied_wormhole[node] = True
                if distance[end] > distance[node] + cost:
                    distance[end] = distance[node] + cost
    
    for node in range(n):
        if distance[node] == float('inf'):
            continue
        for end, cost in graph[node]:
            if cost < 0:
                visitied_wormhole[node] = True            
            if distance[end] > distance[node] + cost:
                return True

    return False

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m, w = map(int, input().split())
        graph = [[] for _ in range(n)]
        for _ in range(m):
            start, end, dist = map(int, input().split())
            start, end = start - 1, end - 1
            graph[start].append((end, dist))
            graph[end].append((start, dist))
        wormholes = set()
        for _ in range(w):
            start, end, dist = map(int, input().split())
            start, end = start - 1, end - 1
            wormholes.add(start)
            graph[start].append((end, -dist))
        
        result = "NO"
        visitied_wormhole = [False] * n
        for wormhole in wormholes:
            if visitied_wormhole[wormhole] == False:
                if negative_cycle_checker(wormhole):
                    result = "YES"
                    break
        print(result)
        


