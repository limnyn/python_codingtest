# https://www.acmicpc.net/problem/17143
'''
구현 문제

[입력]
2 ≤ R, C ≤ 100, 0 ≤ M ≤ R×C
상어는 최대 10000개
낚시왕이 이동하는 거리 100칸
최대 10000 * 100 = 1,000,000 번 연산
'''
import sys
def input(): return sys.stdin.readline().rstrip()


def change_dir(idx):
    if idx == 0:
        return 1
    elif idx == 1:
        return 0
    elif idx == 2:
        return 3
    else:
        return 2
        
def get_first_shark_spot(col):
    '''
    해당 열의 가장 가까운 상어 위치를 반환
    상어가 없으면 -1 반환
    '''
    global grid_r
    for row in range(grid_r):
        # if grid[row][col] != 0:
        if len(grid[row][col]) == 1:
            return row
    return -1    
    
def get_next_shark_spot(shark_r, shark_c, speed, direction):
    global grid_r, grid_c
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]

    if direction < 2:  # 상하 이동 시
        speed %= (grid_r - 1) * 2  # 왕복 거리로 나눈 나머지 이동만 수행
    else:  # 좌우 이동 시
        speed %= (grid_c - 1) * 2

    r, c = shark_r, shark_c
    for _ in range(speed):
        nr = r + dr[direction]
        nc = c + dc[direction]
        if not (0 <= nr < grid_r and 0 <= nc < grid_c):
            direction = change_dir(direction)
            nr = r + dr[direction]
            nc = c + dc[direction]
        r, c = nr, nc
    return r, c, direction

if __name__ == "__main__":
    grid_r, grid_c, m = map(int, input().split())
    grid = [[[] for _ in range(grid_c)] for _ in range(grid_r)]

 
    
    for _ in range(m):
        r, c, s, d, z = map(int, input().split())
        # shark_dq.append((r, c, s, d, z))
        grid[r - 1][c - 1].append((s, d - 1, z))
        

    shark_volume = 0

       
    for col in range(grid_c):
        
        # 1. 낚시왕이 상어를 잡는다
        shark_r = get_first_shark_spot(col)
        if shark_r != -1:
            shark_volume += grid[shark_r][col][0][2]
            grid[shark_r][col] = []
        # 2. 상어들이 이동한다. -> 이동결과는 다음 격자판에 이동시킨다
        next_grid = [[[] for _ in range(grid_c)] for _ in range(grid_r)]
        
        for r in range(grid_r):
            for c in range(grid_c):
                
                if len(grid[r][c]) == 0:
                    continue
                
                speed, direction, volume = grid[r][c][0]
                # 상어의 1초 뒤 위치 계산
                next_r, next_c, next_dir = get_next_shark_spot(r, c, speed, direction)
                
                if len(next_grid[next_r][next_c]): # 이미 상어가 존재한다면
                    fore_shark_volume = next_grid[next_r][next_c][0][2]
                    if fore_shark_volume < volume: # 같은 칸에 있던 상어가 작은 상어면 교체
                        next_grid[next_r][next_c] = [(speed, next_dir, volume)]
                else:
                    next_grid[next_r][next_c] = [(speed, next_dir, volume)]
        
        # 3. 상어 이동한 결과를 반영
        grid = next_grid
    
    # 4. 1~3 반복을 통한 결과 출력
    print(shark_volume)
                
                
                
                
        
        
        
            
# 기존에 작성한 get_next_shark_spot함수 - 시간은 오히려 빠름
# def get_next_shark_spot(shark_r, shark_c, speed, direction):
#     '''
#     1. 이동 시 좌표가 0 또는 n-1을 벗어난다면
#         0 또는 n-1 까지 이동한 다음
#         이동한 만큼 거리를 빼고
#         방향을 뒤집는다
#         다시 반복한다.
#     2. 이동 시 좌표가 벗어나지 않는다면
#         방향 만큼 이동한다.
#     3. 이동이 끝나는 좌표를 반환한다.
#     '''
#     global grid_r, grid_c
    
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, 1, -1]

#     left_distance = speed
#     r = shark_r
#     c = shark_c
#     while left_distance > 0:
#         nr = dr[direction] * left_distance
#         nc = dc[direction] * left_distance
        
#         if direction < 2: # 상하 이동 시
#             nr = r + nr
#             if not (0 <= nr < grid_r):
#                 # 벗어난다면 현재칸에서 끝까지 이동시키고 방향 전환
#                 if direction == 0:
#                     left_distance -= r
#                     r = 0
#                 if direction == 1:
#                     left_distance -= (grid_r - 1 - r)
#                     r = grid_r - 1
#                 direction = change_dir(direction)
            
#             else: # 벗어나지 않는 경우
#                 r = nr
#                 left_distance = 0
                
#         elif direction >= 2: # 좌우 이동시
#             nc = c + nc
#             if not (0 <= nc < grid_c):
#                 # 벗어난다면 현재칸에서 끝까지 이동시키고 방향 전환
#                 if direction == 3:
#                     left_distance -= c
#                     c = 0
#                 if direction == 2:
#                     left_distance -= (grid_c - 1 - c)
#                     c = grid_c - 1
#                 direction = change_dir(direction)
            
#             else: 
#                 c = nc
#                 left_distance = 0
#     return r, c, direction
    


# 시간빠른 코드
# from sys import stdin
# input = stdin.readline

# def main():
#     answer = 0
#     R, C, M = map(int, input().split())
#     sharks = {}
#     top = R+1
    
#     for _ in range(M):
#         # 위치, 속력, 이동방향, 크기
#         r, c, s, d, z = map(int, input().split())
#         sharks[(r, c)] = [s, d, z]
#         if c == 1:
#             top = min(top, r)
        
#     for king_index in range(1, C+1):
#         new_sharks = {}
#         if (top, king_index) in sharks:
#             answer += sharks.pop((top, king_index))[2]
        
#         top = R+1
#         for key, value in sharks.items():
#             r, c = key
#             s, d, z = value
            
#             if d <= 2:
#                 state = r-1 if d==2 else 2*R-r-1
#                 state = (state + s) % (2*R-2)
#                 if state < R:
#                     nr, nc, nd = state+1, c, 2
#                 else:
#                     nr, nc, nd = 2*R-state-1 , c, 1
#             else:
#                 state = c-1 if d==3 else 2*C-c-1
#                 state = (state + s) % (2*C-2)
#                 if state < C:
#                     nr, nc, nd = r, state+1, 3
#                 else:
#                     nr, nc, nd = r , 2*C-state-1, 4
                    
#             if (nr, nc) in new_sharks:
#                 if (new_sharks[(nr, nc)][2] < z):
#                     new_sharks[(nr, nc)] = [s, nd, z]
#             else:
#                 new_sharks[(nr, nc)] = [s, nd, z]
#                 if nc == king_index + 1:
#                     top = min(top, nr)
#         sharks = new_sharks
#     print(answer)
    
# if __name__ == "__main__":
#     main()