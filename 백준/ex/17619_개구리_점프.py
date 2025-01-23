# https://www.acmicpc.net/problem/17619
"""
[문제]
두 개의 통나무 번호가 주어졌을 때, 이동할 수 있는지 확인

[접근]
1. 이동 가능 판별
    먼저 통나무들을 좌표에 따라 정렬하고
    두 통나무의 좌표를 따라 서로 교집합이 존재할 때 이동 가능하다고 판별한다.
2. 분리 집합
    Union Find를 통해 이동가능한 통나무끼리 구분한다.
    이후 두 통나무가 주어지면 같은 그룹인지 아닌지에 따라 출력한다.
"""
import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    # 입력
    n, q = map(int, input().split())
    logs = []
    for i in range(1, n + 1):
        x1, x2, _ = map(int, input().split())
        logs.append((x1, x2, i))

    # 좌표 정렬
    logs.sort(key=lambda x: (x[0], x[1]))
    
    # Union-Find 초기화
    parent = list(range(n + 1))
    rank = [0] * (n + 1)

    # 그룹 초기화
    group_l, group_r = logs[0][0], logs[0][1]
    for i in range(1, n):
        left, right, idx = logs[i]
        if left <= group_r:  # 교집합 존재
            group_r = max(group_r, right)
            union(logs[i - 1][2], idx, parent, rank)
        else:  # 새 그룹 시작
            group_l, group_r = left, right

    # 쿼리 처리
    for _ in range(q):
        n1, n2 = map(int, input().split())
        if find(n1, parent) == find(n2, parent):
            print(1)
        else:
            print(0)

def union(a, b, parent, rank):
    root_a = find(a, parent)
    root_b = find(b, parent)
    if root_a != root_b:
        if rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        elif rank[root_a] < rank[root_b]:
            parent[root_a] = root_b
        else:
            parent[root_b] = root_a
            rank[root_a] += 1

def find(a, parent):
    if parent[a] != a:
        parent[a] = find(parent[a], parent)
    return parent[a]

if __name__ == "__main__":
    main()
