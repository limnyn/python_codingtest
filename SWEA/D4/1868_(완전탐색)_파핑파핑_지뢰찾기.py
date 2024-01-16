
'''
dq = deque()

while dq
    지뢰가 아닌 a에 대해 
    a = dq.popleft()
    
    1, 주변을 탐색하는 함수를 만들고 결과 반환
        1-1 만약 결과가 0이면 주변 8방향에 대해 다시 수행
    
'''
from collections import deque
# 주변을 탐색하는 함수를 만들고 다음 넣을것들을
def serach_around_mine(grid, r, c):
    # r,c의 주변 8방향을 탐색하고
    # 주변의 0인 부분 까지 다시 q에 넣는다
    next_sets = []
    dr = [-1,-1,-1,0,1,1,1,0]
    dc = [-1,0,1,1,1,0,-1,-1]
    mine_count = 0
    for i in range(8):
        nr, nc = r+dr[i], c+dc[i]
        n = len(grid)
        if 0<=nr<n and 0<=nc<n:
            if grid[nr][nc] == '*':
                mine_count+=1
            elif grid[nr][nc] == '.':
                next_sets.append([nr,nc])
    grid[r][c] = mine_count
    return next_sets # 다음 주변 탐색할 리스트들 반환

dq = deque([])



# def full_track(grid, start_r, start_c):
    
    

# for t_c in range(1, int(input())+1):
#     n = int(input())
    
#     grid = [input() for _ in range(n)]
    


    