# https://www.acmicpc.net/problem/1939
"""
[문제]
N개의 섬으로 이루어진 나라에서 몇개의 섬은 다리가 설치되어 있다.

각 다리에는 중량 제한이 있다.

한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 구하기


[입력]
N, M
다음 M개의 줄에는 다리에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다
A, B 섬 사이에 중량 제한이 C인 다리가 존재한다는 의미.

서로 같은 두 섬 사이에 여러 개의 다리가 있을 수 있다.
또한 모든 다리는 양방향이다.
마지막 줄에는 공장이 위치해 있는 섬의 번호를 나타내는 서로 다른 두 정수가 주어진다.

[제약]
1 <= A, B <= N <= 10,000
1 <= C <= 1,000,000,000

시간복잡도 상 N^2까진 가능하다.

[목표]
두 섬을 지나는 경로 중 물건을 가장 많이 적재할 수 있는 경우 구하기

[접근]
1. bfs 이분탐색
    최소 중량제한 간선을 지정하고 가능/불가능에 따라 중량제한을 이분탐색으로 풀기

2. 내림차순 크루스칼
    크루스칼 MST연결 시 그래프 간선 가중치를 오름차순이 아닌 내림차순으로 풀기

"""
import sys
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().rstrip()

# 유니온-파인드
def find_parent(u, parent):
    if parent[u] != u:
        parent[u] = find_parent(parent[u], parent)
    return parent[u]

def union(u, v, parent, rank):
    root_u = find_parent(u, parent)
    root_v = find_parent(v, parent)
    if root_u != root_v:
        if rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        elif rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

def kruskal_max_min_path(graph, n, start, end):
    # 간선들을 가중치 내림차순으로 정렬
    edges = sorted(graph, key=lambda x: -x[2])  # (u, v, weight)

    parent = list(range(n))
    rank = [0] * n

    for u, v, weight in edges:
        # A와 B가 연결되는지 확인
        union(u, v, parent, rank)
        if find_parent(start, parent) == find_parent(end, parent):
            return weight  # 최소 간선 가중치가 최대가 되는 순간의 간선 가중치 반환

    return -1  # 경로가 없을 경우

if __name__ == "__main__":
    n, m = map(int, input().split())

    graph = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph.append((a - 1, b - 1, c))  # 0-based index로 변환
    
    start, end = map(int, input().split())
    start, end = start - 1, end - 1
    result = kruskal_max_min_path(graph, n, start, end)
    print(result)
