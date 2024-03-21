'''

문제 
    1. 모든 섬을 연결하는 경우 중에서
    2. 연결된 간선의 길이의 최소를 구하기

접근
    섬의 갯수  1 <= N <= 1000

    모든 섬에 대한 서로의 거리를 계산하는 경우의 수
    1000c2 -> 1000*999/2 = 499500

    그래프 중 모든 노드를 "연결" 한다면
    최소 신장 트리를 적용해 볼 수 있다.

    최소 신장 트리
        "모든" 노드가 연결 되기 때문에
        
        1. 특정 노드를 선택해서 집합에 넣고
        2. 해당 집합의 간선 중 아직 방문안한 가장 가까운 노드 선택
        3. 1 - 2 반복
        
        을 통해서 구할 수 있을 것 같다

'''
def solution():
    # 입력
    n = int(input())
    grid = [[-1]*(n) for _ in range(n)]
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    E = float(input())
    spots = [(x_list[i],y_list[i], i) for i in range(n)]

    from itertools import combinations
    combs = combinations(spots, 2)

    # 거리 그리드 생성
    for comb in combs:
        start = comb[0]
        end = comb[1]
        dist = (start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2

        grid[start[2]][end[2]] = dist

    # 노드 별 거리를 힙으로 저장
    import heapq
    heaps = []
    for i in range(n):
        for j in range(n):
            distance = grid[i][j]
            if distance != -1:
                heapq.heappush(heaps, (distance, j))
    


    # 힙에 대해서 mst 수행

    # start = 0 # 0번 노드에서 수행
    visited = [False] * n

    result = 0
    mst_node_count = 1
    while mst_node_count < n:

        start_node = heapq.heappop(heaps)
        
        end = start_node[1]

        if visited[end] == True:
            continue
        
        visited[end] = True
        result += start_node[0]
        mst_node_count += 1



    return round(result * E)
    # return result * E

for t_c in range(1, int(input())+ 1):
    print(f"#{t_c} {solution()}")

'''
def solution():
    # 입력
    n = int(input())
    grid = [[-1]*(n) for _ in range(n)]
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    E = float(input())
    spots = [(x_list[i],y_list[i], i) for i in range(n)]

    from itertools import combinations
    combs = combinations(spots, 2)

    # 거리 그리드 생성
    for comb in combs:
        start = comb[0]
        end = comb[1]
        dist = (start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2
        grid[start[2]][end[2]] = (dist, end[2])
        grid[end[2]][start[2]] = (dist, start[2])

    # 노드 별 거리를 힙으로 저장
    import heapq
    heaps = []
    for gr in grid:
        hp = []
        for distance in gr:
            if distance != -1:
                heapq.heappush(hp, distance)
        heaps.append(hp)
    # print(heaps)


    # 힙에 대해서 mst 수행

    start = 0 # 0번 노드에서 수행
    visited = [False] * n
    visited[start] = True
    union = [start]
    result = 0
    for _ in range(n):

        min_dist = (float('inf'),-1)
        min_dist_idx = -1
        for s in union:
            while heaps[s]:
                
                node = heaps[s][0]
                if visited[node[1]] == False:
                    if min_dist[0] > node[0]:
                        if min_dist_idx != -1:
                            heapq.heappush(heaps[min_dist_idx], min_dist)
                        min_dist = heapq.heappop(heaps[s])
                        min_dist_idx = s
                    # else:
                        # node.heapq.heappush(s, node)
                    break
                else:
                    heapq.heappop(heaps[s])

        if min_dist_idx == -1:
            break
        # print(min_dist)
        visited[min_dist[1]] = True
        union.append(min_dist[1])
        result += min_dist[0]

    return round(result * E)
    # return result * E

for t_c in range(1, int(input())+ 1):
    print(f"#{t_c} {solution()}")

'''