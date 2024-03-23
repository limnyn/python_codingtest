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
        
        1. 그룹에 노드 하나를 넣는다
        2. 넣는 노드의 간선 중 방문안한 간선들을 최소힙에 넣는다

        3. 최소힙에서 하나를 꺼내서 방문을 했는지 확인한다.
        4. 만약 방문했다면 1 - 2 - 3을 확인한다.

        5. 노드의 개수 만큼 방문했다면 return 하고 결과를 출력한다
        
        위 과정을 통해서 구할 수 있을 것 같다

'''
import heapq

def solution():
    # 입력
    n = int(input())
    grid = [[-1]*(n) for _ in range(n)]
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    E = float(input())
    spots = [(x_list[i],y_list[i]) for i in range(len(x_list))]



    # 힙에 대해서 mst 수행

    visited = [False] * n
    
    start = 0 # 0번 노드에서 수행
    group_heap = []
    heapq.heappush(group_heap, (0, 0))
    group_cnt = 0
    result = 0

    while group_heap:
        dist, end = heapq.heappop(group_heap)
        
        # 방문하지 않았다면
        if visited[end] == False:
            group_cnt += 1
            result += dist
            # 방문처리하고
            visited[end] = True

            # 새로 그룹에 추가되는 노드에 연결된 간선 중 방문하지 않은 간선들을 힙에 넣는다
            for i in range(n):
                if visited[i] == False:
                    distance = (spots[i][0] - spots[end][0]) ** 2 + (spots[i][1] - spots[end][1]) ** 2
                    heapq.heappush(group_heap, (distance, i))
                    
        if group_cnt == n:
            break
    return round(result * E)



for t_c in range(1, int(input())+ 1):
    print(f"#{t_c} {solution()}")

