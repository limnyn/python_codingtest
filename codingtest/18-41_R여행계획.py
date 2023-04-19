# 한올이가 사는 나라에는 N개의 여행지가 있으며, 각 여행지는 1 ~ N번까지의 번호로 구분됩니다.
# 또한 임의의 두 여행지 사이에는 두 여행지를 연결하는 도로가 존재할 수 있습니다.
# 이때, 여행지가 도로로 연결되어 있다면 양방향으로 이동이 가능하다는 의미입니다.
# 한울이는 하나의 여행 계획을 세운 뒤에 이 여행 계획이 가능한지의 여부를 판단하고자 합니다.
# 예를 들어 N = 5이고, 다음과 같이 도로의 정보가 주어졌다고 가정합시다.

#     1번 여행지 - 2번 여행지
#     1번 여행지 - 4번 여행지
#     1번 여행지 - 5번 여행지
#     2번 여행지 - 3번 여행지
#     2번 여행지 - 4번 여행지

# 만약 한울이의 여행 계획이 2번 -> 3번 -> 4번 -> 3번이라고 해봅시다.
# 이 경우 2번 -> 3번 -> 2번 -> 4번 -> 2번 -> 3번의 순서로 여행지를 방문하면, 여행 계획을 따를 수 있습니다.
# 여행지의 개수와 여행지 간의 연결 정보가 주어졌을 때, 한울이의 여행 계획이 가능한지의 여부를 판별하는 프로그램을 작성하세요.

# 입력 조건
#     첫째 줄에 여행지의 수 N과 여행 계획에 속한 도시의 수 M이 주어집니다.
#     다음 N개의 줄에 걸쳐 N x N 행렬을 통해 임의의 두 여행지가 서로 연결되어 있는지의 여부가 주어집니다.
#     그 값이 1이라면 서로 연결되었다는 의미이며, 0이라면 서로 연결되어 있지 않다는 의미입니다.
#     마지막 줄에 한울이의 여행 계획에 포함된 여행지의 번호들이 주어지며 공백으로 구분합니다.
    
# 출력 조건
#     첫째 줄에 한울이의 여행계획이 가능하다면 YES를, 불가능하다면 NO를 출력합니다.
    
# 입력 예시
# 5 4
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3

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
        
# 여행지의 개수와 여행 계획에 속한 여행지의 개수 입력받기
n, m = map(int, input().split())
parent = [0] * (n + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

#union 연산을 각각 수행행
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    for j in range(1, n + 1):
        if data[j-1] == 1:
            union_parent(parent, i, j)

# 여행 계획 입력받기
plan = list(map(int,input().split()))

result = True
# 여행 계획에 속하는 모든 노드의 루트가 동일한지 확인
for i in range(m - 1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
        result = False

# 여행 계회에 속하는 모든 노드가 서로 역녈되어 있는지(루트가 동일한지) 확인
if result:
    print("YES")
else:
    print("NO")
