# https://www.acmicpc.net/problem/16562
"""
[문제]
가정 적은 비용으로 모든 사람과 친구가 되는 방법 구하기

[접근]
친구의 친구는 친구다. 따라서
1. 친구 집단끼리 집합을 만든다.
2. 각 집단에서의 최소 값을 기반으로 친구비용을 더한다
"""
import sys
def input(): return sys.stdin.readline().rstrip()

def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)  # 경로 압축
    return parent[x]

def union(a, b, parent, rank):
    root_a = find(a, parent)
    root_b = find(b, parent)

    if root_a != root_b:
        if rank[root_a] < rank[root_b]:
            parent[root_a] = root_b
        elif rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        else:
            parent[root_b] = root_a
            rank[root_a] += 1

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    costs = list(map(int, input().split()))
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)

    for _ in range(m):
        src, dst = map(int, input().split())
        union(src, dst, parent, rank)

    # 모든 노드의 루트 갱신
    for i in range(1, n + 1):
        find(i, parent)

    # 각 그룹의 최소 비용 계산
    group_min_cost = {}
    for i in range(1, n + 1):
        root = parent[i]
        if root not in group_min_cost:
            group_min_cost[root] = costs[i - 1]
        else:
            group_min_cost[root] = min(group_min_cost[root], costs[i - 1])

    result = sum(group_min_cost.values())

    if k >= result:
        print(result)
    else:
        print("Oh no")
