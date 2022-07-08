# 입력 조건
#     첫쨰 줄에 동빈이가 듣고자 하는 강의의 수 N(1 <= N <= 500)이 주어진다.
#     다은 N개의 줄에는 각 강의의 강의 시간과 그 강의를 듣기 위해 먼저 들어야 하는 강의들의 번호가 자연수로 주어지며, 각 자연수는 공백으로 구분한다.
#     이때 강의 시간은 100,000 이하의 자연수이다.
#     각 강의 번호는 1부터 N까지로 구성되며, 각 줄은 -1로 끝난다.

# 출력 조건
#     N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 한 줄에 하나씩 출력한다.

# 입력 예시
#     5
#     10 - 1
#     10 1 -1
#     4 1 -1
#     4 3 1 -1
#     3 3 -1

# 출력 예시
#     10
#     20
#     14
#     18
#     17
from collections import deque

# 노드의 개수와 간선의 개수를 입력받기
v = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]
cost = [0] * (v+1)
# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, v+1):
    line = list(map(int, input().split()))
    cost[i] = line[0]
    for j in range(line[1:-1]):
        graph[line[j]].append(i) 
        indegree[i] += 1

# 위상정렬 함수
def topology_sort():
    result = cost[:] # 알고리즘 수행결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 떄는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 떄까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[now]+cost[i], result[i])
            # 새롭게 진입차수가 0이되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # # 위상 정렬을 수행한 결과 출력
    for i in range(1, v+1):
        print(result[i])

topology_sort()

# 시간복잡도 O(V + E)


