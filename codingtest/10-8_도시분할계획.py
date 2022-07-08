# 입력 조건
#     첫째 줄에 집의 개수 N, 길의 개수 M이 주어진다. 
#     N은 2 이상 100,000 이하인 정수이고, M은 1 이상 1,000,000 이하인 정수이다.
#     그다음 줄부터 M줄에 걸쳐 길의 정보가 A, B, C 3개의 정수로 공백으로 구분되어 주어지는데 
#     A번 집과 B번 집을 연결하는 길의 유지비가 C (1 <= C <= 1,000)라는 뜻이다.

# 출력 조건
#     첫째 줄에 길을 없애고 남은 유지비 합의 최솟값을 출력한다.

# 입력 예시
#     7 12
#     1 2 3
#     1 3 2
#     3 2 1
#     2 5 2
#     3 4 4
#     7 3 6
#     5 1 5
#     1 6 2
#     6 4 1
#     6 5 3
#     4 5 3 
#     6 7 4

# 출력 예시 
#     8

# 최소신장트리 만들고 제일 큰 가중치 간선 제거하기


# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i


# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용 순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
maxcost = 0
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        maxcost = cost

print(result-maxcost)

# 시간복잡도 O(ElogE)