# BFS == 너비 우선 탐색
# 가까운 노트부터 탐색하는 알고리즘

# BFS 구현에서는 스택 대신 큐 자료구조를 이용한다

# 동작 방식
    # 1. 탐색 시작 노드를 큐에 삽입
    # 2. 큐에서 노드르 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
    # 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

# BFS알고리즘은 큐 자료구조에 기초, 구현이 간단ㄷ하다.
# deque 라이브러를 사용하고, 탐색 수행에 O(N)의 시간이 소요된다.
# 실제 수행시간도 DFS보다 좋은편이다.

# 5-9.py BFS 예제

from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문처리
    visited[start] = True
    # 큐가 빌때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9


# 정의된 BFS 함수 호출
bfs(graph, 1, visited)