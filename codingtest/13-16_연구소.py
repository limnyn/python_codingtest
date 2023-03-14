# https://www.acmicpc.net/problem/14502




# 입력 끝
import sys
input = sys.stdin.readline
virus = []  #2의 좌표(r,c)들
index0 = [] #0의 좌표(r,c)들
lab_map = []    

n, m = map(int, input().split())
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 2:
          virus.append((i,j))  
        elif line[j] == 0:
            index0.append((i, j))
    lab_map.append(line)
        
    
import collections
def bfs(test_map, virus):
    queue = collections.deque(virus)
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    while(queue):
        px, py = queue.popleft()
        for i in range(4):
            x = px + dx[i]
            y = py + dy[i]
            if x < 0 or y < 0 or x >= n or y >= m:
                continue
            elif test_map[x][y] == 0:
                test_map[x][y] = 2
                queue.append((x,y))
            else:
                continue


import copy
def safe_area_max(lab_map, cols):
    test_map = copy.deepcopy(lab_map)
    for i in cols:
        r, c = index0[i]
        test_map[r][c] = 1
    bfs(test_map, virus)
    result = 0
    for i in range(n):
        for j in range(m):
            if test_map[i][j] == 0:
                result += 1

    return result # 안전지대 반환


import itertools
col_list = list(itertools.combinations([x for x in range(0, len(index0))],3))
prev_max =  0
for cols in col_list: 
    prev_max = max(prev_max, safe_area_max(lab_map, cols))
print(prev_max)
