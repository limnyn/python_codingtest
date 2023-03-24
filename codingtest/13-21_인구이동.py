# https://www.acmicpc.net/problem/16234


import sys
from collections import deque
input = sys.stdin.readline
n, l, r = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int,input().split())))

 

dx = [1, 0, -1 ,0]
dy = [0, -1, 0 ,1]

result = 0

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def process(x, y, index):
    # (x, y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
    united = []
    united.append((x, y))
    # 너비 우선 탐색(BFS)를 위한 큐 자료구조 정의
    q = deque()
    q.append((x,y))
    union[x][y] = index # 현재 연합의 번호 할당
    summary = grid[x][y] # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 국가 수
    # 큐가 빌 때까지 반복
    while q:
        x, y = q.popleft()
        # 현재 위치에서 4가지 방향을 확인하며
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 옆에 있는 나라를 확인하여
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 옆에 있는 나라와 인구 차이가 L명 이상, R명 이하라면
                if l <= abs(grid[nx][ny] - grid[x][y]) <= r:
                    q.append((nx,ny))
                    # 연합에 추가
                    union[nx][ny] = index
                    summary += grid[nx][ny]
                    count += 1
                    united.append((nx, ny))
    # 엽합 국가끼리 인구를 분배
    for i, j in united:
        grid[i][j] = summary // count
    return count

total_count = 0

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 해당 나라가 아직 처리되지 않았다면
                process(i, j, index)
                index += 1 
    # 모든 인구 이동이 끝난 경우
    if index == n * n:
        break
    total_count += 1
    
# 인구 이동 횟수 출력
print(total_count)

                     
                     
                     
# # https://www.acmicpc.net/problem/16234


# # dfs로 다 순회할 때 x,y좌표들을 리스트에 넣고 왔다감 표시를 blobs에 한다.
# # 순회가 끝나면 setlist에 좌표모음을 넣는다
# # 모든 좌표에 대해 수행한다.
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
# n, left, right = map(int, input().split())
# grid = []
# for _ in range(n):
#     grid.append(list(map(int,input().split())))

 

# dx = [1, 0, -1 ,0]
# dy = [0, -1, 0 ,1]


# def dfs(sets:list ,r,c):
#     for i in range(4):
#         x = r + dx[i]
#         y = c + dy[i]
        
#         if x < 0 or y < 0 or x >= n or y >= n:
#             continue
#         if blobs[x][y] != 0:
#             continue
        
#         dif = abs(grid[r][c] - grid[x][y])
#         if dif <= right and dif >= left:
#             blobs[x][y] = -1
#             sets.append((x,y,grid[x][y]))
#             dfs(sets, x, y)



# day = 0
# while(1):
#     setlist = []
#     blobs = [[0] * n for _ in range(n)]
#     for r in range(n):
#         for c in range(n):
#             if blobs[r][c] == -1:
#                 continue
#             is_in = False
#             for sets in setlist:
#                 if (r,c,grid[r][c]) in sets:
#                     is_in = True
#             if is_in == True:
#                 continue
#             s = [(r,c,grid[r][c])]
#             blobs[r][c] = -1
#             dfs(s, r, c)
   
#             # s = set(s)
#             setlist.append(s)
#     # print(setlist)
#     if len(setlist) == n*n:
#         break
    
#     for aset in setlist:
#         setavg = 0
#         for x, y, a in aset:
#             setavg += a
#         setavg //= len(aset)
#         for x, y, a in aset:
#             grid[x][y] = setavg
            
#     day += 1
    
        
# print(day)
