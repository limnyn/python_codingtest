# https://www.acmicpc.net/problem/18428

#N이 6일때 최대이다. 장애물은 3개를 설치하므로 36*35*34 = 42840, 충분히 계산 가능한 수치이다.

import sys, copy
from itertools import combinations
input = sys.stdin.readline
n = int(input())
grid = []
teachers = []
students = []
unblocked = []
for r in range(n):
    line = list(input().split())
    for c in range(len(line)):
        if line[c] == 'S':
            students.append((r,c))
        elif line[c] == 'T':
            teachers.append((r,c))
        elif line[c] == 'X':
            unblocked.append((r,c))
    grid.append(line)


def dfs(grid,teachers,students):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    for teacher in teachers:
        for i in range(4):
            x, y =teacher[0], teacher[1]
            while(1):
                x += dx[i]
                y += dy[i]
                if not (x>=0 and x < n and y >= 0 and y < n):
                    break
                if grid[x][y] == 'O' or grid[x][y] == 'T':
                    break
                elif grid[x][y] == 'X':
                    continue
                elif grid[x][y] == 'S':
                    # stu_count -= 1
                    return False
                    grid[x][y] == 'X'
    return True
                        
                    
def solutions(grid, teachers, students):
        
    blocks = list(combinations(unblocked,3))
    for block in blocks:
        newblocks = copy.deepcopy(grid)
        for r, c in block:
            newblocks[r][c] = 'O'
        if dfs(newblocks, teachers, students):
            return "YES"
    return "NO"

print(solutions(grid, teachers, students))
        

    
        