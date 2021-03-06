# 입력 조건
#     첫째 줄에 전체 회사의 개수 N과 경로의 개수 M이 공백으로 구분되어 차례대로 주어진다.(1<=N, M<=100)
#     둘째 줄부터 M + 1 번째 줄에는 연결된 두 회사의 번호가 공백으로 구분되어 주어진다.
#     M + 2번째 줄에는 X와 K가 공백으로 구분되어 차례대로 주어진다. (1 <= K <= 100)

# 출력 조건
#     첫째 줄에 방문 판매원 A가 K번 회사를 거쳐 X번 회사로 가는 최소 이동시간을 출력한다.
#     만약 X번 회사에 도달할 수 없다면 -1을 출력한다.

# 입력 예시 1
    # 5 7
    # 1 2
    # 1 3
    # 1 4
    # 2 4
    # 3 4
    # 3 5
    # 4 5
    # 4 5

# 출력 예시 1
#     3


# 입력 예시 2
#     4 2
#     1 3
#     2 4
#     3 4

# 출력 예시 2
#     -1
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]
# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
x,k = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

if graph[1][k] >= INF or graph[k][x] >= INF:
    print("-1")
# 도달할 수 있는 경우 거리를 출력
else:
    print(graph[1][k] + graph[k][x])

