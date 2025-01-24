# https://www.acmicpc.net/problem/20040
'''
[문제]
입력이 주어졌을때
1. 사이클이 완성되었는지
2. 완성되었다면 몇번째 입력에서 사이클이 완성되었는지

[접근]

Unionfind
    1. 각 간선을 하나씩 처리한다.
    2. 두 노드가 이미 같은 집합에 속해있다면, 사이클이 존재한다.
    3. 그렇지 않으면 두 노드를 같은 집한으로 합친다.

    두 노드가 같은 집합에 속해 있다는 것은, 두 노드 간의 경로가 이미 존재한다는 의미로, 사이클을 형성하게 된다.

'''
import sys
def input(): return sys.stdin.readline()

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False # 사이클 발견
        
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True
    
if __name__ == "__main__":
    n, m = map(int, input().split())
    
    count = 0
    union_find = UnionFind(n)
    edges = []
    
    for _ in range(m):
        a, b = map(int, input().split())
        edges.append((a, b))

    for a, b in edges:
        count += 1
        
        if not union_find.union(a, b):
            print(count)
            exit()
    
    print(0)
    



