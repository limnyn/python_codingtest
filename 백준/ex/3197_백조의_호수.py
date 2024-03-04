# https://www.acmicpc.net/problem/3197
"""
1. 백조 A,= start,  B = end
3. swanspot | next_swanspot
2. waterspot | next_waterspot
4. day += 1 하고 2~3 반복


"""
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

# for g in grid:
#     print(g)


from collections import deque
swan_spot = deque()
water_spot = deque()
next_swan_spot = deque()
next_water_spot = deque()

swan_visited = [[False] * m for _ in range(n)]
water_visited = [[False] * m for _ in range(n)]

end = []
for r in range(n):
    for c in range(m):
        if grid[r][c] == 'L':
            if len(swan_spot) == 0:
                swan_spot.append((r,c))                
                swan_visited[r][c] = True
            else:
                end = [r,c]
            water_spot.append((r,c))
            water_visited[r][c] = True
            grid[r][c] = '.'
        elif grid[r][c] == '.':
            water_spot.append((r,c))
            water_visited[r][c] = False



dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]        
def melt_ice():
    while water_spot:
        r, c = water_spot.popleft()
        grid[r][c] = '.'
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m and water_visited[nr][nc] == False:
                if grid[nr][nc] == '.':
                    water_spot.append((nr,nc))
                elif grid[nr][nc] == 'X':
                    next_water_spot.append((nr,nc))
                water_visited[nr][nc] = True

def swan_domain():
    while swan_spot:
        r, c = swan_spot.popleft()
        if r == end[0] and c == end[1]:
            return True
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m and swan_visited[nr][nc] == False:
                if grid[nr][nc] == '.':
                    swan_spot.append((nr,nc))
                elif grid[nr][nc] == 'X':
                    next_swan_spot.append((nr,nc))
                swan_visited[nr][nc] = True
    return False

days = 0
while True:
    melt_ice()
    if swan_domain():
        break
    
    water_spot = next_water_spot
    swan_spot = next_swan_spot
    next_swan_spot = deque()
    next_water_spot = deque()
    
    days += 1
print(days)


            
            
##집합으로 나누어서 풀었던거 시간초과 났던 코드
# https://www.acmicpc.net/problem/3197
# """
# 1. 백조의 A, B의 호수를 1, 2번으로 지정
# 2. 나머지 호수들에 대해서 3부터 n까지 지정해준다
# 3. 각 호수들에 대해 첫 테두리(bfs로 퍼져나가며 x와 닿은 .좌표들)을 구한다

# 4. edge에 대해  다음 지울 x좌표들 delete_spot[[r,c,set_num]] 구한다
# 5. delete_spot에 대해 대해
#     if grid[r][c] == 'X':
#         grid[r][c] = '.'
#         visited[r][c] = set_num
#         for i in range(4):
#             if visited[nr][nc] != 0 and not in union:
#                 union(grid[r][c], set_num)
#                 if 백조A and 백조B in union:
#                     day를 출력하고 멈춘다
#     elif grid[r][c] == '.'
#         if grid[r][c] not in Union: -> 만약 set_num가 grid[r][c]와 연합이 아니라면
#             union(grid[r][c], set_num)
#             if 백조A and 백조B in union:
#                 day를 출력하고 멈춘다
    
#     edge.append([r,c, set_num])

#     days+=1
# 6. 4~5를 반복

# """


# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# grid = []
# swan_spot = []
# for r in range(n):
#     line = list(input())
#     for c in range(m):
#         if line[c] == 'L':
#             swan_spot.append([r,c])
#     grid.append(line)
    

# visited = []
# # for g in grid:
# #     print(g)

# # print(swan_spot)

# dr = [-1, 0, 1, 0]
# dc = [0, -1, 0, 1]
# visited = [[0]*m for _ in range(n)]
# from collections import deque
# edges = []

# # next = []
# def bfs(start_r, start_c, set_num):
#     global visited
#     dq = deque([])

#     visited[start_r][start_c] = set_num
#     dq.append([start_r,start_c])

#     while dq:
#         r, c = dq.popleft()
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if 0 <= nr < n and 0 <= nc < m:
#                 if visited[nr][nc] == 0:
#                     if grid[nr][nc] == '.':
#                         visited[nr][nc] = set_num
#                         dq.append([nr,nc])
#                     elif grid[nr][nc] == 'X':
#                         edges.append((nr, nc,set_num))
# set_count = 1
# sets = []
# dict_for_unions = {}
# for i in range(2):
#     sets.append(set([set_count]))
#     dict_for_unions[set_count] = set([set_count])
#     bfs(swan_spot[i][0], swan_spot[i][1], set_count)         
#     set_count+=1


# for r in range(n):
#     for c in range(m):
#         if visited[r][c] == 0 and grid[r][c] == '.':
#             sets.append(set([set_count]))
#             dict_for_unions[set_count] = set([set_count])
#             bfs(r,c,set_count)
#             set_count+=1

# def union_and_update(num1, num2):
#     s1 = dict_for_unions[num1]
#     s2 = dict_for_unions[num2]
#     s3 = s1.union(s2)
#     sets.remove(s1)
#     sets.remove(s2)
#     sets.append(s3)
#     for a in s3:
#         dict_for_unions[a] = s3

# def is_unioned(num1, num2):
#     s1 = dict_for_unions[num1]
#     if num2 in s1:
#     # if len(s1.difference(s2)) == 0: #차집합의 길이가 0이면
#         return True
#     else:
#         return False
        

# tmp_visited = []
# # 4번 다음 지울 얼음 칸들 찾기
# def find_delete():
#     global tmp_visited, edges
#     tmp_visited = [[False]*m for _ in range(n)]
#     next_delete_spot = []
#     for r, c, s_num in edges:
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#             if 0 <= nr < n and 0 <= nc < m:
#                 if grid[nr][nc] == 'X' and tmp_visited[nr][nc] == False:
#                     tmp_visited[nr][nc] = True
#                     next_delete_spot.append((nr,nc,s_num))
#     edges = next_delete_spot

# # 5번 얼음 삭제 진행 및 연합 찾기
# def delete_ice():
#     global edges
#     new_edge = []
#     for r, c, s_num in edges:
#         if grid[r][c] == 'X':
#             grid[r][c] = '.'
#             visited[r][c] = s_num
#             for i in range(4):
#                 nr = r + dr[i]
#                 nc = c + dc[i]
                
#                 if 0 <= nr < n and 0 <= nc < m:
#                     if visited[nr][nc] != 0:
#                         if not is_unioned(s_num, visited[nr][nc]):
#                             union_and_update(s_num, visited[nr][nc])
#                             if is_unioned(1, 2):
#                                 print(days)
#                                 return True
#                     if visited[nr][nc] == 0 and grid[nr][nc] == 'X':
#                         new_edge.append((r,c,s_num))
#         elif grid[r][c] == '.':
#             if not is_unioned(visited[r][c], s_num):
#                 union(s_num, visited[nr][nc])
#                 if is_unioned(1, 2):
#                     print(days)
#                     return True
        
#     edges = new_edge
#     return False



# days = 1
# while True:
#     if delete_ice():
#         break
#     days += 1
#     find_delete()



