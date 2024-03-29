# 당신은 화성 탐사 기계를 개발하는 프로그래머입니다. 
# 그런데 화성은 에너지 공급원을 찾기가 힘듭니다.
# 그래서 에너지를 효율적으로 사용하고자 화성 탐사 기계가 출발 지점에서 목표 지점까지 이동 할 때 항상 최적의 경로를 찾도록 개발해야 합니다.
# 화성 탐사 기계가 존재하는 공간은 NxN 크기의 2차원 공간이며, 각각의 칸을 지나기 위한 비용(에너지 소모량)이 존재합니다.
# 가장 왼쪽 위 칸인 [0][0] 위치에서 가장 오른쪽 아래 칸인 [N - 1][N - 1] 위치로 이동하는 최소 비용을 출력하는 프로그램을 작성하세요.
# 화성 탐사 기계는 특정한 위치에서 상하좌우 인접한 곳으로 1칸씩 이동할 수 있습니다.

# 입력 조건
#     첫째 줄에 테스트 케이스의 수 T (1<=T<=10)가 주어집니다.
#     매 테스트 케이스의 첫째 줄에는 탐사 공간의 크기를 의미하는 정수 N이 주어집니다. (2 <= N <= 125)
#     이어서 N개의 줄에 걸쳐 각 칸의 비용이 주어지며 공백으로 구분합니다.(0 <= 각 칸의 비용 <= 9)

# 출력 조건
#     각 테스트 케이스마다 [0][0]의 위치에서 [N-1][N-1]의 위치로 이동하는 최소 비용을 한 줄에 하나씩 출력합니다.

# 입력 예시
# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4

# 출력 예시
# 20
# 19
# 36
    
    
import sys, heapq
input = sys.stdin.readline

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정
def shortcut(n):
    dx = [-1, 0,1 , 0]
    dy = [0, 1, 0, -1]
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
        
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance =  [[INF] * n for _ in range(n) ]
    x, y = 0, 0 # 시작 위치는 (0, 0)
    # 시작 노드로 가기 위한 비용은 (0, 0) 위치의 값으로 설정하여, 큐에 삽입
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]
                    
    # 다익스트라 알고리즘 수행
    while q:
        # 가장 최단거리가 짧은 노드에 대한 정보를 꺼내기
        dist, x, y = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[x][y] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵의 범위를 벗어나는 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
                
    return distance[n-1][n-1]
                    
    # floyd[0][0] = graph[0][0]
    # for k in range(n):
    #     for a in range(n):
    #         for b in range(n):
    #             floyd[a][b] = min(floyd[a][b],floyd[a][k] + floyd[k][b])
    
result = []
for _ in range(int(input())):
    result.append(shortcut(int(input())))

for r in result: print(r)




# # 해설
#     맵의 각 위치를 노드로 보고 상하좌우로 모든 노드가 연결되어 있다고 보면 된다.
#     A와 B가 서로 인접해 있다고 할 때 
#     A - B와 B - A의 비용은 도착지의 탐사비용이 된다.
    
#     2차원 공간이기 때문에 전채 노드의 개수는 n^2으로 10000을 넘을 수 있다
#     따라서 플로이드 워셜 알고리즘으로는 이 문제를 해결하기 적합하지 않으므로 다익스트라 알고리즘을 이용한다.