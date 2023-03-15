#https://www.acmicpc.net/problem/18405

import collections, sys

input = sys.stdin.readline



n, k = map(int, input().split())

grid = []
virus_spot = []

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        if line[j] != 0:
            virus_spot.append((line[j],i,j))
    grid.append(line)
end_time, last_r, last_c = map(int, input().split())


def bfs(grid, virus_spot):      # queue에 들어있는 값들에 대해 4방향 탐색을 하고 , 탐색한 지점들을 넣은 리스트를 반환한다.
    queue = collections.deque(sorted(virus_spot))
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    new_virus_spot = []
    
    while(queue):
        q = queue.popleft()
        num, px, py = q[0], q[1], q[2]
        for i in range(4):
            x = px + dx[i]
            y = py + dy[i]
            if x < 0 or y < 0 or x >= n or y >= n or (grid[x][y] != 0 and num > grid[x][y]):
                continue
            elif grid[x][y] == 0:
                grid[x][y] = num
                new_virus_spot.append((num, x,y))
            else:
                continue
    return new_virus_spot

for i in range(end_time):
    virus_spot = bfs(grid, virus_spot)
print(grid[last_r-1][last_c-1])


#틀린 풀이
#틀린 이유
    # 입력시 바로 정렬되게 heapq에 넣었는데
    # heap은 그자체로 정렬되는게 아니라 pop시에 출력을 순서대로 해줄 뿐이다
    # 따라서 heap을 queue로 변환한다고 정렬되는것이 아니다.
    # heapq 부분을 list로 대체하고 함수실행시 정렬되게 고쳤다.
# import heapq, collections, sys

# input = sys.stdin.readline



# n, k = map(int, input().split())

# grid = []
# virus_spot = []

# for i in range(n):
#     line = list(map(int, input().split()))
#     for j in range(len(line)):
#         if line[j] != 0:
#             heapq.heappush(virus_spot,(line[j],i,j))
#     grid.append(line)
# end_time, last_r, last_c = map(int, input().split())


# def bfs(grid, virus_spot):
#     queue = collections.deque(virus_spot)
#     dx = [-1,0,1,0]
#     dy = [0,-1,0,1]
#     new_virus_spot = []
    
#     while(queue):
#         q = queue.popleft()
#         num, px, py = q[0], q[1], q[2]
#         for i in range(4):
#             x = px + dx[i]
#             y = py + dy[i]
#             if x < 0 or y < 0 or x >= n or y >= n or (grid[x][y] != 0 and num > grid[x][y]):
#                 continue
#             elif grid[x][y] == 0:
#                 grid[x][y] = num
#                 heapq.heappush(new_virus_spot, (num, x,y))
#             else:
#                 continue
#     return new_virus_spot

# for i in range(end_time):
#     virus_spot = bfs(grid, virus_spot)
    
# print(grid[last_r-1][last_c-1])
